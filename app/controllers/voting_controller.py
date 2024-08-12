# app/controllers/voting_controller.py
from flask import request, jsonify
import app.services.voting_service as vote_mgr

def create_vote():
    """Accept votes."""
    data = request.get_json()
    if not data or 'user_id' not in data or 'vote' not in data:
        return jsonify({"error": "Invalid input data."}), 400
    
    vote_data = vote_mgr.cast_vote(data['user_id'], data['vote'])
    return jsonify(vote_data), 201

def get_all_votes():
    """Get all votes."""
    votes = vote_mgr.get_votes()
    return jsonify(votes), 200

def get_votes_for_user(user_id):
    """Get vote for given user id."""
    votes = vote_mgr.get_votes_by_user(user_id)
    if not votes:
        return jsonify({"error": "User not found."}), 404
    
    return jsonify(votes), 200
