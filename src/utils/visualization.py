# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(data):
    """
    Visualize the data.

    Args:
        data (pandas.DataFrame): DataFrame containing the data to visualize.

    Returns:
        None
    """
    # Example visualization: Pairplot
    sns.pairplot(data)
    plt.title("Pairplot of Data")
    plt.show()

def visualize_model_performance(model, X, y):
    """
    Visualize the performance of the predictive maintenance model.

    Args:
        model (PredictiveMaintenanceModel): Trained predictive maintenance model.
        X (array-like, shape (n_samples, n_features)): Input data.
        y (array-like, shape (n_samples,)): True labels.

    Returns:
        None
    """
    # Example visualization: Confusion matrix
    y_pred = model.predict(X)
    confusion_matrix = pd.crosstab(y, y_pred, rownames=['Actual'], colnames=['Predicted'])
    sns.heatmap(confusion_matrix, annot=True, fmt='g', cmap='Blues')
    plt.title("Confusion Matrix")
    plt.show()

