# app/dto/vote.py

import uuid

class Vote:
    def __init__(self, user_id, vote):
        self.id = str(uuid.uuid4())  # Use UUID for custom id
        self.user_id = user_id
        self.vote = vote

    def to_dict(self):
        return {
            "_id": self.id,  # Use id as _id
            "user_id": self.user_id,
            "vote": self.vote
        }
