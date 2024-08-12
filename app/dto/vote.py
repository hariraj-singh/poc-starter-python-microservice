# app\dto\vote.py

import uuid

class Vote:
    def __init__(self, user_id, vote):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.vote = vote

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "vote": self.vote
        }
