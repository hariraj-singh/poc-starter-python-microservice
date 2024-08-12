# app\controllers\sample_controller.py
from flask import request, jsonify

def get_greeting():
    """Returns a greeting message."""
    return {"message": "Hello, World!"}, 200

def create_greeting():
    """Creates a custom greeting message."""
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Invalid input data."}), 400
    name = data['name']
    return {"message": f"Hello, {name}!"}, 201
