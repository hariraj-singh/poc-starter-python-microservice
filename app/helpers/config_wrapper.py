import yaml
import copy


class Config:
    _config = None

    @classmethod
    def load_config(cls, file_path="config.yaml"):
        """Load configuration from a YAML file."""
        with open(file_path, "r") as file:
            cls._config = yaml.safe_load(file)

    @classmethod
    def get_config(cls):
        """Get the loaded configuration."""
        if cls._config is None:
            cls.load_config()
        return cls._config

    @classmethod
    def get_config_as_dict(cls):
        """Get the configuration as a dictionary."""
        if cls._config is None:
            cls.load_config()
        # Return a deep copy of the config to ensure the original config is not altered
        return copy.deepcopy(cls._config)
