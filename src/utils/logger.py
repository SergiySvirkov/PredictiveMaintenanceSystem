# logger.py

import logging

class Logger:
    def __init__(self, log_file="predictive_maintenance.log"):
        """
        Initialize the logger.

        Args:
            log_file (str): Path to the log file.
        """
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Create a file handler and set the logging level
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)

        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)

        # Add the file handler to the logger
        self.logger.addHandler(file_handler)

    def info(self, message):
        """
        Log an information message.

        Args:
            message (str): Message to log.
        """
        self.logger.info(message)

    def error(self, message):
        """
        Log an error message.

        Args:
            message (str): Message to log.
        """
        self.logger.error(message)
