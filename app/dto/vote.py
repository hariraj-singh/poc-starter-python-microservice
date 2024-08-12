import uuid


class Base_DTO:
    pass


class Vote:
    def __init__(self, **kwargs):
        self.vote_id = kwargs.get("vote_id") or str(uuid.uuid4())
        self.user_id = kwargs.get("user_id")
        self.vote_value = kwargs.get("vote_value")

    def __post_init__(self):
        self.validate_vote()

    def validate_vote(self):
        """Validate vote object"""
        if len(self.user_id) <= 5:
            raise ValueError("user_id has to be minimum 5 characters")
        if len(self.vote_value) == 0:
            raise ValueError("vote has to be minimum 1 characters")

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(**dict_obj)
