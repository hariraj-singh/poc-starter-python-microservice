# app/helpers/database_wrapper.py
from pymongo import MongoClient


class DatabaseWrapper:
    DB_VOTE_COLLECTION = "votes"

    def __init__(self):
        username = "admin"
        password = "password"
        host = "localhost"
        port = 27017
        database_name = "voting_db"
        uri = f"mongodb://{username}:{password}@{host}:{port}"
        self.client = MongoClient(uri)
        self.db = self.client[database_name]

    def get_collection(self, collection_name):
        """Retrieve a collection by name."""
        return self.db[collection_name]
