#test split_data
import os
import pandas as pd
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.data_split import data_split

@pytest.fixture
def synthetic_data():
    return pd.DataFrame({
        'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [6, 7, 8, 9, 10],
        'Target': [0, 1, 0, 1, 0]
    })

@pytest.mark.parametrize("train_file, test_file", [
    ("train_data.csv", "test_data.csv"),
    ("train.csv", "test.csv"),
    ("train_split.csv", "test_split.csv")
])
def test_data_split(synthetic_data, train_file, test_file):
    data_split(synthetic_data, train_file, test_file)

    # check if the train and test CSV files have been created
    assert os.path.isfile(train_file)
    assert os.path.isfile(test_file)

    # read the train and test files
    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)

    # checks if data was split
    assert len(train_df) > 0
    assert len(test_df) > 0
    assert len(train_df) + len(test_df) == len(synthetic_data)

    os.remove(train_file)
    os.remove(test_file)
