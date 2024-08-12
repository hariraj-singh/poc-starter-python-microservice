# app\dto\vote.py
from app.dto.base_dto import Base_DTO
import uuid


class Vote(Base_DTO):
    def __init__(self, **kwargs):
        self.vote_id = kwargs.get("vote_id") or str(uuid.uuid4())
        self.user_id = kwargs.get("user_id")
        self.vote_value = kwargs.get("vote_value")

        # Call to validate the object
        self.validate_vote()

    def validate_vote(self):
        """Validate vote object"""
        if self.user_id == None or len(self.user_id) <= 5:
            raise ValueError("user_id has to be minimum 5 characters")
        if self.vote_value == None or len(self.vote_value) == 0:
            raise ValueError("vote has to be minimum 1 characters")
