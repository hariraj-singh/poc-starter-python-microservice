# app\helpers\exception_handler.py
from flask import jsonify
import logging

# Set up a logger for the exception handlers
logger = logging.getLogger(__name__)


def handle_value_error(e):
    """Handle ValueErrors and return a 400 response."""
    # Log the exception details
    logger.warning(f"A ValueError occurred: {str(e)}")

    # Create a custom response for ValueErrors
    response = {"error": "Input Error", "message": str(e)}

    # Return the response as JSON with a 400 status code
    return jsonify(response), 400


def handle_exception(e):
    """Handle general exceptions and return a custom response."""
    # Log the exception details
    logger.error(f"An error occurred: {str(e)}", exc_info=True)

    # Create a custom response for other exceptions
    response = {"error": "An unexpected error occurred.", "message": str(e)}

    # Return the response as JSON with a 500 status code
    return jsonify(response), 500
