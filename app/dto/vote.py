import uuid


class Vote:
    def __init__(self, **kwargs):
        self.id = kwargs.get("id") or str(
            uuid.uuid4()
        )  # Generate a new UUID for each Vote
        self.user_id = kwargs.get("user_id")
        self.vote = kwargs.get("vote")

    def __post_init__(self):
        self.validate_vote()

    def validate_vote(self):
        if len(self.user_id) <= 5:
            raise ValueError("user_id has to be minimum 5 characters")

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_obj):
        return cls(**dict_obj)
