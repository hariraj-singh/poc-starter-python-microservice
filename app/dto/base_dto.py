class Base_DTO:
    def to_dict(self):
        """Convert the object to a dictionary."""
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_obj):
        """Create an object from a dictionary."""
        return cls(**dict_obj)
