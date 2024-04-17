# main.py

import json
from data_processing.data_loader import load_data
from data_processing.data_preprocessing import preprocess_data
from data_processing.feature_engineering import engineer_features
from model.train import train_model
from utils.logger import Logger
from utils.visualization import visualize_data, visualize_model_performance
from config.config import Config

def main():
    # Load configuration
    config = Config()

    # Initialize logger
    logger = Logger()

    # Load raw sensor data
    logger.info("Loading raw sensor data...")
    raw_data = load_data(config.data_path)

    # Preprocess data
    logger.info("Preprocessing data...")
    preprocessed_data = preprocess_data(raw_data)

    # Engineer features
    logger.info("Engineering features...")
    engineered_features = engineer_features(preprocessed_data)

    # Train model
    logger.info("Training model...")
    model = train_model(engineered_features, config.model_params)

    # Visualize data
    logger.info("Visualizing data...")
    visualize_data(engineered_features)

    # Visualize model performance
    logger.info("Visualizing model performance...")
    visualize_model_performance(model, engineered_features)

if __name__ == "__main__":
    main()
