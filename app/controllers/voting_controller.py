# app\controllers\voting_controller.py
from flask import request, jsonify
import uuid


all_votes=[]


def create_vote():
    """Accept votes"""
    data = request.get_json()
    if not data or 'user_id' not in data or 'vote' not in data:
        return jsonify({"error": "Invalid input data."}), 400
    
    vote_id = uuid.uuid4()
    data["vote_id"] = vote_id
    all_votes.append(data)
    return jsonify(data), 201

def get_all_votes():
    """Get all votes"""
    global all_votes
    return jsonify(all_votes), 200

def get_votes_for_user(user_id):
    """Get vote for given user"""
    global all_votes
    votes = [vote for vote in all_votes if vote['user_id'] == user_id]
    if votes==None or len(votes) ==0:
        return jsonify({"error": "Vote not found."}), 404
    
    return jsonify(votes), 200

