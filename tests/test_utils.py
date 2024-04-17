# test_utils.py

import pytest
from utils.logger import Logger

@pytest.fixture
def sample_logger():
    # Sample logger instance
    return Logger(log_file="test.log")

def test_logger_initialization(sample_logger):
    # Test logger initialization
    assert hasattr(sample_logger, 'logger')  # Check if logger object exists
    assert len(sample_logger.logger.handlers) == 1  # Check if only one handler is added

def test_logger_info(sample_logger, capsys):
    # Test logging information message
    sample_logger.info("Test info message")
    captured = capsys.readouterr()
    assert "Test info message" in captured.out  # Check if message is logged correctly

def test_logger_error(sample_logger, capsys):
    # Test logging error message
    sample_logger.error("Test error message")
    captured = capsys.readouterr()
    assert "Test error message" in captured.err  # Check if error message is logged correctly

