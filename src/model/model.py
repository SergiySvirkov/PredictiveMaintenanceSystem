# model.py

from sklearn.ensemble import RandomForestClassifier

class PredictiveMaintenanceModel:
    def __init__(self, model_params=None):
        """
        Initialize the predictive maintenance model.

        Args:
            model_params (dict): Parameters for the model.
        """
        if model_params is None:
            # If no parameters provided, use default settings for RandomForestClassifier
            self.model = RandomForestClassifier()
        else:
            # Initialize RandomForestClassifier with provided parameters
            self.model = RandomForestClassifier(**model_params)

    def train(self, X_train, y_train):
        """
        Train the predictive maintenance model.

        Args:
            X_train (array-like, shape (n_samples, n_features)): Training data.
            y_train (array-like, shape (n_samples,)): Target labels.

        Returns:
            None
        """
        # Fit the model to the training data
        self.model.fit(X_train, y_train)

    def predict(self, X):
        """
        Make predictions using the trained model.

        Args:
            X (array-like, shape (n_samples, n_features)): Input data.

        Returns:
            array-like, shape (n_samples,): Predicted labels.
        """
        # Predict labels for input data
        return self.model.predict(X)

    def predict_proba(self, X):
        """
        Return probability estimates for the predictions.

        Args:
            X (array-like, shape (n_samples, n_features)): Input data.

        Returns:
            array-like, shape (n_samples, n_classes): Probability estimates.
        """
        # Return probability estimates for each class
        return self.model.predict_proba(X)
