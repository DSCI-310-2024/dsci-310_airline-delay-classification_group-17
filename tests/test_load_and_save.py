import os
import pandas as pd
import sys
import pickle
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.load_and_save import load_data, save_model

@pytest.fixture
def sample_data():
    """Create sample data for testing."""
    return pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})

@pytest.fixture
def sample_model():
    """Create a sample model for testing."""
    return {'param1': 0.5, 'param2': 'abc'}

def test_load_data(tmp_path, sample_data):
    """Test load_data function."""
    file_path = tmp_path / "test.csv"
    sample_data.to_csv(file_path, index=False)
    loaded_data = load_data(file_path)
    assert isinstance(loaded_data, pd.DataFrame)
    assert sample_data.equals(loaded_data)

def test_save_model(tmp_path, sample_model):
    """Test save_model function."""
    file_path = tmp_path / "test_model.pickle"
    save_model(sample_model, file_path)
    assert os.path.exists(file_path)
    with open(file_path, 'rb') as f:
        loaded_model = pickle.load(f)
    assert loaded_model == sample_model
