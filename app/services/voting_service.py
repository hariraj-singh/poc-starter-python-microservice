# app/services/voting_service.py

from app.helpers.database_wrapper import DatabaseWrapper
from app.dto.vote import Vote

# Initialize the database wrapper
db_wrapper = DatabaseWrapper()
votes_collection = db_wrapper.get_collection('votes')

def cast_vote(user_id, vote_value):
    """Cast a new vote and store it in MongoDB with a custom id."""
    vote = Vote(user_id, vote_value).to_dict()
    votes_collection.insert_one({**vote})  # Explicitly set _id
    return vote

def get_votes():
    """Retrieve all votes from MongoDB."""
    votes = list(votes_collection.find({}))
    # for vote in votes:
    #     vote['id'] = str(vote['_id'])
    return votes

def get_votes_by_user(user_id):
    """Retrieve all votes for a specific user from MongoDB."""
    votes = list(votes_collection.find({'user_id': user_id}))
    # for vote in votes:
    #     vote['id'] = str(vote['_id'])
    return votes