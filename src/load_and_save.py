import pandas as pd
import pickle

def load_data(file_path):
    """Load data from a CSV file."""
    return pd.read_csv(file_path)

def save_model(model, file_path):
    """Save a trained model to a file using pickle."""
    with open(file_path, 'wb') as f:
        pickle.dump(model, f)
