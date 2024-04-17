# data_loader.py

import pandas as pd

def load_data(data_path):
    """
    Load raw sensor data from a CSV file.

    Args:
        data_path (str): Path to the CSV file containing raw sensor data.

    Returns:
        pandas.DataFrame: DataFrame containing the loaded raw sensor data.
    """
    try:
        # Load data from CSV file
        raw_data = pd.read_csv(data_path)

        # Optionally, perform additional data loading steps such as parsing dates, etc.

        return raw_data
    except FileNotFoundError:
        print(f"Error: File '{data_path}' not found.")
        return None
