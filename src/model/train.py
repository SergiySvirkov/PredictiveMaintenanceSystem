# train.py

from sklearn.model_selection import train_test_split
from model.model import PredictiveMaintenanceModel

def train_model(engineered_features, model_params):
    """
    Train the predictive maintenance model.

    Args:
        engineered_features (pandas.DataFrame): DataFrame containing engineered features.
        model_params (dict): Parameters for the model.

    Returns:
        PredictiveMaintenanceModel: Trained predictive maintenance model.
    """
    # Split the data into features (X) and target (y)
    X = engineered_features.drop(columns=['target_column'])
    y = engineered_features['target_column']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the predictive maintenance model
    model = PredictiveMaintenanceModel(model_params)

    # Train the model on the training data
    model.train(X_train, y_train)

    # Optionally, evaluate the model on the test data
    # test_accuracy = model.evaluate(X_test, y_test)

    return model

