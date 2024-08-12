# app/services/voting_service.py

from typing import List, Optional
from app.helpers.database_wrapper import DatabaseWrapper
from app.dto.vote import Vote

# Initialize the database wrapper
db_wrapper = DatabaseWrapper()
votes_collection = db_wrapper.get_collection(db_wrapper.DB_VOTE_COLLECTION)


def cast_vote(vote: Vote) -> Vote:
    """Cast a new vote and store it in MongoDB with a UUID as _id."""
    # Store Vote into db and then retrieve the object.
    votes_collection.insert_one(vote.to_dict())
    db_vote = votes_collection.find_one({"vote_id": vote.vote_id})

    # Cast db object to DTO and return
    rt_vote = Vote.from_dict(db_vote) if db_vote else None
    return rt_vote


def get_votes() -> Optional[List[Vote]]:
    """Retrieve all votes from Database."""
    db_votes = votes_collection.find()
    if not db_votes:
        return None

    return [Vote.from_dict(vote) for vote in db_votes]


def get_votes_by_user(user_id: str) -> Optional[List[Vote]]:
    """Retrieve all votes for a specific user from Database."""
    db_users_votes = votes_collection.find({"user_id": user_id})
    if not db_users_votes:
        return None

    return [Vote.from_dict(vote) for vote in db_users_votes]
