# app.py

import connexion
from connexion.resolver import RestyResolver


def main():
    # Create the Connexion application instance
    app = connexion.App(__name__, specification_dir="api/spec")

    # Read the OpenAPI spec from the yaml file
    app.add_api("openapi.yaml", resolver=RestyResolver("api"))

    # Run the application
    app.run(port=8080)


if __name__ == "__main__":
    main()
