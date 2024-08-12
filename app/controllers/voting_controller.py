# app/controllers/voting_controller.py
from flask import request, jsonify
import app.services.voting_service as vote_mgr
from app.dto.vote import Vote
import json


def create_vote():
    """Accept votes."""
    data_dict = request.get_json()
    dto_vote = Vote.from_dict(data_dict)

    vote_data = vote_mgr.cast_vote(dto_vote)
    xx = vote_data.to_dict()
    return jsonify(xx), 201


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
