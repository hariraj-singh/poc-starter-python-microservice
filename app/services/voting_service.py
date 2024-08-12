# app/services/voting_service.py

from app.helpers.database_wrapper import DatabaseWrapper
from app.dto.vote import Vote

# Initialize the database wrapper
db_wrapper = DatabaseWrapper()
votes_collection = db_wrapper.get_collection(db_wrapper.DB_VOTE_COLLECTION)


def cast_vote(vote: Vote) -> Vote:
    """Cast a new vote and store it in MongoDB with a UUID as _id."""
    votes_collection.insert_one(vote.to_dict())
    stored_vote = votes_collection.find_one({"vote_id": vote.vote_id})
    rt_vote = Vote.from_dict(stored_vote) if stored_vote else None
    return rt_vote


def get_votes():
    """Retrieve all votes from Database."""
    db_votes = votes_collection.find()
    return [Vote.from_dict(vote) for vote in db_votes]


def get_votes_by_user(user_id):
    """Retrieve all votes for a specific user from Database."""
    db_users_votes = votes_collection.find({"user_id": user_id})
    return [Vote.from_dict(vote) for vote in db_users_votes]
