# read raw data

import pandas as pd
import pytest

# import read from 01_filter-raw-data.py
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.01_filter-raw-data.py import read

# test the read function and if it returns a DataFrame
def test_read():
    file_name = 'data/raw/full_data_flightdelay.csv'
    assert isinstance(read(file_name), pd.DataFrame)