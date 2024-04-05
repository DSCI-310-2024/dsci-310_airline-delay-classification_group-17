# filter raw data

import os
import sys
import pandas as pd
import pytest

# path to import function into scripts
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.filter_columns import filter_columns

# Ftest data fixture
@pytest.fixture
def test_data():
    return pd.DataFrame({
        'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]
    })

# ilter_columns return dataframe with the correct columns test
def test_filter_columns(test_data):
    list_of_features_and_target = ['A', 'B']
    filtered_data = filter_columns(test_data, list_of_features_and_target)
    assert list(filtered_data.columns) == list_of_features_and_target

# filter_columns test with empty list
def test_filter_columns_empty_list(test_data):
    with pytest.raises(ValueError):
        filter_columns(test_data, [])

# filter_columns test with non existing columns
def test_filter_columns_non_existing_columns(test_data):
    with pytest.raises(KeyError):
        filter_columns(test_data, ['NON_EXISTING_COLUMN'])

# filter_columns empty dataframe test
def test_filter_columns_empty_data():
    empty_df = pd.DataFrame()
    with pytest.raises(ValueError):
        filter_columns(empty_df, ['COLUMN'])

# filter_columns test with NONE data
def test_filter_columns_none_data():
    with pytest.raises(TypeError):
        filter_columns(None, ['COLUMN'])