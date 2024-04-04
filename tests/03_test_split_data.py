# split data into train and test

import pandas as py
import pytest

# import read from 02_split_data.py
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.01_filter-raw-data.py import read, data_split

# test data split function to confirm that it returns a train and test split data
def test_train_test_split():
    filtered_data = read("data/processed/01_filtered-data.csv")

    data_split()

    # read the train and test sets from csv files
    flight_train = pd.read_csv("data/processed/02_flight-train.csv")
    flight_test = pd.read_csv("data/processed/02_flight-test.csv")

    # check if train and test sets are DataFrame objects
    assert isinstance(flight_train, pd.DataFrame)
    assert isinstance(flight_test, pd.DataFrame)

    # check if the total number of rows in train and test sets add up to the total number of rows in the filtered data
    assert len(flight_train) + len(flight_test) == len(filtered_data)

    # check if train and test sets have the same columns as the filtered data
    assert all(flight_train.columns == filtered_data.columns)
    assert all(flight_test.columns == filtered_data.columns)