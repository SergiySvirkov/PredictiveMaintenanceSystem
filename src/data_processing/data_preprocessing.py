# data_preprocessing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

def preprocess_data(raw_data):
    """
    Preprocess raw sensor data.

    Args:
        raw_data (pandas.DataFrame): DataFrame containing raw sensor data.

    Returns:
        pandas.DataFrame: DataFrame containing preprocessed sensor data.
    """
    if raw_data is None:
        return None

    # 1. Handling missing values
    preprocessed_data = raw_data.dropna()

    # 2. Removing irrelevant columns
    columns_to_keep = ['relevant_feature_1', 'relevant_feature_2', 'relevant_feature_3']
    preprocessed_data = preprocessed_data[columns_to_keep]

    # 3. Standardization or normalization of numeric features
    numeric_features = ['numeric_feature_1', 'numeric_feature_2']
    scaler = StandardScaler()
    preprocessed_data[numeric_features] = scaler.fit_transform(preprocessed_data[numeric_features])

    # 4. Encoding categorical features
    categorical_features = ['categorical_feature']
    label_encoder = LabelEncoder()
    preprocessed_data[categorical_features] = label_encoder.fit_transform(preprocessed_data[categorical_features])

    return preprocessed_data

