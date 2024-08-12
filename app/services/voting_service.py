# app/services/voting_service.py

from app.dto.vote import Vote

# This should ideally be a database or persistent storage.
all_votes = []

def cast_vote(user_id, vote_value):
    """Cast a new vote."""
    vote = Vote(user_id, vote_value).to_dict()
    all_votes.append(vote)
    return vote

def get_votes():
    """Retrieve all votes."""
    return all_votes

def get_votes_by_user(user_id):
    """Retrieve votes for a specific user."""
    return [vote for vote in all_votes if vote['user_id'] == user_id]
