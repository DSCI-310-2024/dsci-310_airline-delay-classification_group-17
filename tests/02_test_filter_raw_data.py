# filter raw data

import pandas as py
import pytest

# import read from 01_filter-raw-data.py
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.01_filter-raw-data.py import filter_columns

# test if filter_columns returns a DataFrame with the correct colums
def test_filter_columns():
    file_name = 'data/raw/full_data_flightdelay.csv'
    list_of_features_and_target = ['MONTH', 'DAY_OF_WEEK', 'DEP_DEL15', 'CONCURRENT_FLIGHTS', 'CARRIER_NAME',
                                   'FLT_ATTENDANTS_PER_PASS', 'GROUND_SERV_PER_PASS', 'PLANE_AGE', 'SNOW', 'AWND']
    raw_data = pd.read_csv(file_name)
    filtered_data = filter_columns(raw_data, list_of_features_and_target)
    assert list(filtered_data.columns) == list_of_features_and_target