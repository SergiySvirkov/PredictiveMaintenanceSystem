# feature_engineering.py

import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif
from sklearn.preprocessing import PolynomialFeatures

def engineer_features(preprocessed_data):
    """
    Engineer features from preprocessed sensor data.

    Args:
        preprocessed_data (pandas.DataFrame): DataFrame containing preprocessed sensor data.

    Returns:
        pandas.DataFrame: DataFrame containing engineered features.
    """
    if preprocessed_data is None:
        return None

    # 1. Feature selection
    X = preprocessed_data.drop(columns=['target_column'])
    y = preprocessed_data['target_column']
    selector = SelectKBest(score_func=f_classif, k=3)
    selected_features = selector.fit_transform(X, y)

    # Convert selected_features array back to DataFrame
    selected_features_df = pd.DataFrame(selected_features, columns=X.columns[selector.get_support()])

    # 2. Feature transformation
    poly_features = PolynomialFeatures(degree=2)
    transformed_features = poly_features.fit_transform(selected_features_df)

    # Convert transformed_features array back to DataFrame
    transformed_features_df = pd.DataFrame(transformed_features, columns=poly_features.get_feature_names(selected_features_df.columns))

    # 3. Feature aggregation
    aggregated_features = preprocessed_data.groupby('grouping_column').agg({'numeric_feature': ['mean', 'std', 'max']})

    return transformed_features_df, aggregated_features

