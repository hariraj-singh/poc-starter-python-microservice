from typing import List, Optional
from app.helpers.database_wrapper import DatabaseWrapper
from app.helpers.kafka_wrapper import KafkaWrapper
from app.dto.vote import Vote
import logging

# Set up a logger for the exception handlers
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO
)  # You can set the level to DEBUG for more detailed output

# Initialize the database wrapper
db_wrapper = DatabaseWrapper()
votes_collection = db_wrapper.get_collection(db_wrapper.DB_VOTE_COLLECTION)

# Initialize the Kafka wrapper
kafka_wrapper = KafkaWrapper()
topic_name = "votes_topic"  # Specify the Kafka topic you want to use


def cast_vote(vote: Vote) -> Optional[Vote]:
    """Cast a new vote and store it in MongoDB with a UUID as _id."""

    # Store the vote in the database
    vote_dict = vote.to_dict()
    votes_collection.insert_one(vote_dict)
    db_vote = votes_collection.find_one({"vote_id": vote.vote_id})

    # Cast db object to DTO and return
    rt_vote = Vote.from_dict(db_vote) if db_vote else None

    if rt_vote:
        # Publish a message to Kafka
        kafka_wrapper.publish_message(
            topic=topic_name, key=str(vote.vote_id), value=rt_vote
        )
        logger.info(f"Vote {vote.vote_id} published to Kafka topic {topic_name}.")

    return rt_vote


def get_votes() -> Optional[List[Vote]]:
    """Retrieve all votes from Database."""
    db_votes = votes_collection.find()
    return [Vote.from_dict(vote) for vote in db_votes] if db_votes else None


def get_votes_by_user(user_id: str) -> Optional[List[Vote]]:
    """Retrieve all votes for a specific user from Database."""
    db_users_votes = votes_collection.find({"user_id": user_id})
    return [Vote.from_dict(vote) for vote in db_users_votes] if db_users_votes else None
