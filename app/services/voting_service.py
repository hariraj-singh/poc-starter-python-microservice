# app/services/voting_service.py

from app.helpers.database_wrapper import DatabaseWrapper
from app.dto.vote import Vote

# Initialize the database wrapper
db_wrapper = DatabaseWrapper()
votes_collection = db_wrapper.get_collection("votes")


def cast_vote(user_id, vote_value):
    """Cast a new vote and store it in MongoDB with a UUID as _id."""
    vote = Vote(user_id, vote_value)
    # Convert the Vote object to a dictionary and insert it into MongoDB
    votes_collection.insert_one(
        {
            "_id": vote.id,  # Use the generated UUID as the document ID
            "user_id": vote.user_id,
            "vote": vote.vote,
        }
    )
    return vote


def get_votes():
    """Retrieve all votes from MongoDB as Vote objects."""
    votes = votes_collection.find()
    return [Vote(vote["user_id"], vote["vote"], id=vote["_id"]) for vote in votes]


def get_votes_by_user(user_id):
    """Retrieve all votes for a specific user from MongoDB as Vote objects."""
    user_votes = votes_collection.find({"user_id": user_id})
    return [Vote(vote["user_id"], vote["vote"], id=vote["_id"]) for vote in user_votes]
