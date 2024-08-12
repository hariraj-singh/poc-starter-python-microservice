from confluent_kafka import Producer, KafkaException
from pymongo import MongoClient
from app.helpers.config_wrapper import Config
import time, uuid
import logging

logger = logging.getLogger(__name__)


class KafkaWrapper:
    def __init__(self):
        # Load configurations
        config = Config.get_config()

        config_kafka = config["kafka_server"]

        kafka_config = {
            "bootstrap.servers": config_kafka["bootstrap_brokers"],
            "client.id": config_kafka["client_id"],
        }
        mongo_config = {
            "uri": config_kafka["dlq_mongo_database_url"],
            "database": config_kafka["dlq_database_name"],
        }

        self.producer = Producer(kafka_config)
        self.mongo_client = MongoClient(mongo_config["uri"])
        self.mongo_db = self.mongo_client[mongo_config["database"]]

        # Other misc configs
        self.default_partition = config_kafka.get("default_partition", 3)
        self.default_retries = config_kafka.get("default_retries", 3)
        self.default_interval = config_kafka.get("default_interval", 5)

    def delivery_report(self, err, msg):
        if err is not None:
            print(f"Delivery failed for message: {msg.key()}: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    def publish_message(
        self,
        topic: str,
        value,
        key=None,
        partition=None,
        retries=None,
        retry_interval=None,
    ):
        if key is None:
            key = str(uuid.uuid4()).encode("utf-8")  # Ensure the key is a byte string

        if partition is None:
            partition = self.default_partition

        if retries is None:
            retries = self.default_retries

        if retry_interval is None:
            retry_interval = self.default_interval

        retry_count = 0
        success = False

        while retry_count < retries and not success:
            try:
                self.producer.produce(
                    topic,
                    key=key,
                    value=value,
                    partition=partition,
                    callback=self.delivery_report,
                )
                self.producer.flush()
                success = True
            except KafkaException as e:
                logger.warning(
                    f"Error producing message: {e}, retry counter: {retry_count}",
                    exc_info=True,
                )
                retry_count += 1
                time.sleep(retry_interval)

        if not success:
            # Write to MongoDB DLQ collection
            dlq_collection = self.mongo_db[f"DLQ_{topic}"]
            dlq_collection.insert_one(
                {"key": key, "value": value, "error": str(e), "retries": retry_count}
            )
            logger.error(
                f"Message moved to DLQ_{topic} collection after {retry_count} retries.",
                exc_info=True,
            )
