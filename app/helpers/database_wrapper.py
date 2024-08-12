# app/helpers/database_wrapper.py
from pymongo import MongoClient
from app.helpers.config_wrapper import Config


class DatabaseWrapper:
    DB_VOTE_COLLECTION = "votes"

    def __init__(self):
        # Load configurations
        config = Config.get_config()
        mongo_config = config["mongo_database"]

        database_url = mongo_config["database_url"]
        self.client = MongoClient(database_url)

        database_name = mongo_config["database_name"]
        self.db = self.client[database_name]

    def get_collection(self, collection_name):
        """Retrieve a collection by name."""
        return self.db[collection_name]
