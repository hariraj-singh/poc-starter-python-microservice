# app/services/voting_service.py

from app.helpers.database_wrapper import DatabaseWrapper
from app.dto.vote import Vote
from app.helpers.decorators import transform_id

# Initialize the database wrapper
db_wrapper = DatabaseWrapper()
votes_collection = db_wrapper.get_collection('votes')

def cast_vote(user_id, vote_value):
    """Cast a new vote and store it in MongoDB with a UUID as _id."""
    vote = Vote(user_id, vote_value).to_dict()
    votes_collection.insert_one(vote)  # Insert the vote with _id as UUID
    return vote

@transform_id
def get_votes():
    """Retrieve all votes from MongoDB."""
    votes = list(votes_collection.find({}))
    return votes

@transform_id
def get_votes_by_user(user_id):
    """Retrieve all votes for a specific user from MongoDB."""
    votes = list(votes_collection.find({'user_id': user_id}))
    return votes
