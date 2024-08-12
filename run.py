# run.py

import connexion
import logging
from app.helpers.exception_handler import handle_value_error, handle_exception
from app.helpers.config_wrapper import Config

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    config = Config.get_config()

    # Create the Connexion application instance and set the Swagger services
    spec_dir = config["open_api"]["spec_dir"]
    api_doc = config["open_api"]["api_doc"]
    app = connexion.App(__name__, specification_dir=spec_dir)
    app.add_api(api_doc)

    # Register exception Handler
    app.app.register_error_handler(ValueError, handle_value_error)
    app.app.register_error_handler(Exception, handle_exception)

    # Run the application
    app.run(port=config["service"]["port"])


if __name__ == "__main__":
    main()
