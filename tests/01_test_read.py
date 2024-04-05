# read test
import os
import sys
import pandas as pd
import pytest

# path import function
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.read import read

# test data
test_cases = [
    (
        {'Temperature': [25, 30, 27], 'Humidity': [50, 60, 55], 'Wind_Speed': [10, 12, 8]},
        3
    ),  
    (
        {'Population': [1000, 2000, 1500], 'GDP': [50000, 60000, 55000], 'Unemployment_Rate': [5, 6, 4]},
        3
    ), 
]

# read funcito test with multiple cases
def test_read():
    for data, expected_length in test_cases:
       
        # temporary CSV file
        file_name = 'temp_test_file.csv'
        pd.DataFrame(data).to_csv(file_name, index=False)
        
        # read function test
        df = read(file_name)
        assert isinstance(df, pd.DataFrame)
        assert len(df) == expected_length
        # delete temporary file
        os.remove(file_name)

# invalid path read test
def test_read_invalid_path():
    with pytest.raises(FileNotFoundError):
        read('non_existent_file.csv')

# empty file read test
def test_read_empty_file():
    
    # make empty file
    empty_file = 'empty_file.csv'
    open(empty_file, 'a').close()
    with pytest.raises(pd.errors.EmptyDataError):
        read(empty_file)
    os.remove(empty_file)