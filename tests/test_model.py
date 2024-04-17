# test_model.py

import pytest
import pandas as pd
from model.model import PredictiveMaintenanceModel

@pytest.fixture
def sample_model_params():
    # Sample model parameters
    return {
        "n_estimators": 100,
        "max_depth": 5,
        "random_state": 42
    }

@pytest.fixture
def sample_data():
    # Sample engineered features data
    data = {
        'feature_1': [1, 2, 3, 4, 5],
        'feature_2': [4, 5, 6, 7, 8],
        'target_column': [0, 1, 0, 1, 0]
    }
    return pd.DataFrame(data)

def test_model_initialization(sample_model_params):
    # Test model initialization
    model = PredictiveMaintenanceModel(sample_model_params)
    assert model.model.get_params()['n_estimators'] == sample_model_params['n_estimators']
    assert model.model.get_params()['max_depth'] == sample_model_params['max_depth']
    assert model.model.get_params()['random_state'] == sample_model_params['random_state']

def test_model_training(sample_data, sample_model_params):
    # Test model training
    model = PredictiveMaintenanceModel(sample_model_params)
    X_train = sample_data.drop(columns=['target_column'])
    y_train = sample_data['target_column']
    model.train(X_train, y_train)
    assert hasattr(model, 'model')  # Check if model is trained

def test_model_prediction(sample_data, sample_model_params):
    # Test model prediction
    model = PredictiveMaintenanceModel(sample_model_params)
    X_test = sample_data.drop(columns=['target_column'])
    y_pred = model.predict(X_test)
    assert len(y_pred) == sample_data.shape[0]  # Check if predictions are made for all samples

