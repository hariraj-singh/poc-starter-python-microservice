# app.py

import connexion
import logging
from app.helpers.exception_handler import handle_value_error, handle_exception

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    # Create the Connexion application instance and set the Swagger services
    app = connexion.App(__name__, specification_dir="app/controllers/spec")
    app.add_api("openapi.yaml")

    # Register exception Handler
    app.app.register_error_handler(ValueError, handle_value_error)
    app.app.register_error_handler(Exception, handle_exception)

    # Run the application
    app.run(port=8080)


if __name__ == "__main__":
    main()
