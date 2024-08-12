from confluent_kafka import Producer, KafkaException, admin
from pymongo import MongoClient
from app.helpers.config_wrapper import Config
import time, uuid, json
import logging

logger = logging.getLogger(__name__)


class KafkaWrapper:
    def __init__(self):
        # Load configurations
        config = Config.get_config()

        config_kafka = config.get("kafka_server", None)

        kafka_config = {
            "bootstrap.servers": config_kafka.get(
                "bootstrap_brokers", "localhost:29091"
            ),
            "client.id": config_kafka.get("client_id"),
        }
        mongo_config = {
            "uri": config_kafka.get("dlq_mongo_database_url"),
            "database": config_kafka.get("dlq_database_name"),
        }

        self.producer = Producer(kafka_config)
        self.admin_client = admin.AdminClient(kafka_config)
        self.mongo_client = MongoClient(mongo_config.get("uri"))
        self.mongo_db = self.mongo_client[mongo_config.get("database")]

        # Other misc configs
        self.default_partition_count = config_kafka.get("default_partition", 1)
        self.default_replicas = config_kafka.get("default_replicas", 1)
        self.default_retries = config_kafka.get("default_retries", 3)
        self.default_interval = config_kafka.get("default_interval", 5)

    def delivery_report(self, err, msg):
        if err is not None:
            print(f"Delivery failed for message: {msg.key()}: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

    def ensure_topic_exists(self, topic_name):
        """Ensure the topic exists in Kafka."""
        topic_metadata = self.admin_client.list_topics(timeout=10)
        if topic_name not in topic_metadata.topics:
            logger.info(f"Topic {topic_name} does not exist. Creating...")
            new_topic = admin.NewTopic(
                topic_name,
                num_partitions=self.default_partition_count,
                replication_factor=self.default_replicas,
            )
            self.admin_client.create_topics([new_topic])
            logger.info(f"Topic {topic_name} created.")

    def publish_message(
        self,
        topic: str,
        value,
        key=None,
        retries=None,
        retry_interval=None,
    ):
        # Ensure the topic exists before publishing
        self.ensure_topic_exists(topic)

        if key is None:
            key = str(uuid.uuid4()).encode("utf-8")  # Ensure the key is a byte string

        if retries is None:
            retries = self.default_retries

        if retry_interval is None:
            retry_interval = self.default_interval

        retry_count = 0
        success = False

        # Convert the Vote object to a dictionary and then serialize it
        value_dict = value.to_dict()
        value_bytes = json.dumps(value_dict).encode("utf-8")

        retry_error = None

        while retry_count < retries and not success:
            try:
                self.producer.produce(
                    topic,
                    key=key,
                    value=value_bytes,
                    callback=self.delivery_report,
                )
                self.producer.flush()
                success = True
            except KafkaException as e:
                retry_error = e
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
                {
                    "key": key,
                    "value": value_dict,
                    "error": str(retry_error),
                    "retries": retry_count,
                }
            )
            logger.error(
                f"Message moved to DLQ_{topic} collection after {retry_count} retries.",
                exc_info=True,
            )
