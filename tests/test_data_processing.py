# test_data_processing.py

import pytest
import pandas as pd
from data_processing.data_loader import load_data
from data_processing.data_preprocessing import preprocess_data
from data_processing.feature_engineering import engineer_features

@pytest.fixture
def sample_data():
    # Create sample raw sensor data
    data = {
        'feature_1': [1, 2, 3, None, 5],
        'feature_2': [4, 5, 6, 7, 8],
        'target_column': [0, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)

def test_load_data(sample_data):
    # Test data loading
    loaded_data = load_data(sample_data)
    assert loaded_data.shape == (5, 3)

def test_preprocess_data(sample_data):
    # Test data preprocessing
    preprocessed_data = preprocess_data(sample_data)
    assert preprocessed_data.shape[0] == 4  # Check if rows with missing values are dropped

def test_engineer_features(sample_data):
    # Test feature engineering
    engineered_features = engineer_features(sample_data)
    assert engineered_features.shape[1] == 3  # Check if correct number of features is engineered
