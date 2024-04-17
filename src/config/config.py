# config.py

import json

class Config:
    def __init__(self, config_file="config.json"):
        """
        Initialize project configurations.

        Args:
            config_file (str): Path to the configuration file.
        """
        self.config = self.load_config(config_file)

    def load_config(self, config_file):
        """
        Load configurations from a JSON file.

        Args:
            config_file (str): Path to the configuration file.

        Returns:
            dict: Dictionary containing configurations.
        """
        try:
            with open(config_file, 'r') as f:
                config = json.load(f)
                return config
        except FileNotFoundError:
            print(f"Error: Configuration file '{config_file}' not found.")
            return {}

    def get(self, key):
        """
        Get a configuration value by key.

        Args:
            key (str): Key of the configuration value.

        Returns:
            object: Configuration value.
        """
        return self.config.get(key)
