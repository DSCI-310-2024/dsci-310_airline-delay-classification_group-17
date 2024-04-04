# data_split test
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_split import data_split

# test data
@pytest.fixture
def synthetic_data():
    return pd.DataFrame({
        'Feature1': [1, 2, 3, 4, 5],
        'Feature2': [6, 7, 8, 9, 10],
        'Target': [0, 1, 0, 1, 0]
    })

# data_split creating a train and test data CSV file test
def test_data_split(synthetic_data):
    data_split(synthetic_data)

    # check if the respective train and test csv files are created
    assert os.path.isfile("data/processed/02_flight-train.csv")
    assert os.path.isfile("data/processed/02_flight-test.csv")

    # read created files
    flight_train = pd.read_csv("data/processed/02_flight-train.csv")
    flight_test = pd.read_csv("data/processed/02_flight-test.csv")

    # check if data was split correctly
    assert len(flight_train) > 0
    assert len(flight_test) > 0
    assert len(flight_train) + len(flight_test) == len(synthetic_data)

    # clean up
    os.remove("data/processed/02_flight-train.csv")
    os.remove("data/processed/02_flight-test.csv")
