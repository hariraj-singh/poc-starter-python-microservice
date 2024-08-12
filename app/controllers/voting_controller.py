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
    return jsonify(vote_data.to_dict()), 201


def get_all_votes():
    """Get all votes."""
    dto_votes = vote_mgr.get_votes()

    # Convert object to dict so that it can be jsonfied
    return jsonify([v.to_dict() for v in dto_votes]), 200


def get_votes_for_user(user_id):
    """Get vote for given user id."""
    dto_votes = vote_mgr.get_votes_by_user(user_id)
    if not dto_votes:
        return jsonify({"error": "No Votes found for given user."}), 404

    # Convert object to dict so that it can be jsonfied
    return jsonify([v.to_dict() for v in dto_votes]), 200
