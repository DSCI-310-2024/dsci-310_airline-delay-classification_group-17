import pandas as pd
import pytest
import sys
import os

# Import replace_value function from src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.replace_value import replace_value

# Test data
candy_df = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                          'rating':[-5, 0, 5, 80.0]})
candy_df1 = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                          'rating':[-5, 0, 5, 80.0]})
candy_df2 = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                          'rating':[-5, 0, 5, 80.0]})
candy_df3= pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                          'rating':[-5, 0, 5, 80.0]})
candy_df4 = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                          'rating':[-5, 0, 5, 80.0]})
candy_df5 = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                          'rating':[-5, 0, 5, 80.0]})
candy_df6 = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                          'rating':[-5, 0, 5, 80.0]})
empty_df = pd.DataFrame({'candy':[], 'rating':[]})
wrong_input = ['candy corn', 'smarties', 'kitkat', 'coffee crisp']

# Expected outputs
replace_str_output_candy_corn = pd.DataFrame({'candy':['dirt', 'smarties', 'kitkat', 'coffee crisp'],
                                              'rating':[-5, 0, 5, 80.0]})
replace_str_output_kitkat = pd.DataFrame({'candy':['candy corn', 'smarties', 'gold', 'coffee crisp'],
                                          'rating':[-5, 0, 5, 80.0]})
replace_int_output_negative = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                                            'rating':[-10, 0, 5, 80.0]})
replace_int_output_zero = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                                        'rating':[-5, 3, 5, 80.0]})
replace_int_output_positive = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                                            'rating':[-5, 0, 10, 80.0]})
replace_float_output = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'],
                                     'rating':[-5, 0, 5, 100.0]})

# Test for correct error handling for incorrect input type
def test_replace_value_type_error():
    with pytest.raises(TypeError):
        replace_value(wrong_input, 'candy', 'candy corn', 'dirt')
        replace_value(candy_df, 40, 'candy corn', 'dirt')
        replace_value(candy_df, 'candy', ['', ''], 'dirt')
        replace_value(candy_df, 'candy', 'candy corn', ['', ''])

# Test for correct error handling if the specifed column is not in the inputted panda DataFrame
def test_replace_value_exception1():
    with pytest.raises(Exception):
        replace_value(candy_df, 'not a column', 'candy corn', 'dirt')
        replace_value(empty_df, 'candy', 'candy corn', 'dirt')

# Test for correct error handling if the old_value is not in the specified column
def test_replace_value_exception2():
    with pytest.raises(Exception):
        replace_value(candy_df, 'candy', 'not a candy', 'dirt')

# Test for correct return type
def test_replace_value_returns_dataframe():
    result = replace_value(candy_df, 'candy', 'smarties', 'smarties')
    assert isinstance(result, pd.DataFrame), "replace_value should return a pandas DataFrame"

# Test if the function successfully replaces the old value in the specified column with the specified new value
def test_replace_value_str1():
    pd.testing.assert_frame_equal(replace_value(candy_df1, 'candy', 'candy corn', 'dirt'),
                                  replace_str_output_candy_corn)
    pd.testing.assert_frame_equal(replace_value(candy_df2, 'candy', 'kitkat', 'gold'),
                                  replace_str_output_kitkat)
    pd.testing.assert_frame_equal(replace_value(candy_df3, 'rating', -5, -10),
                                  replace_int_output_negative)
    pd.testing.assert_frame_equal(replace_value(candy_df4, 'rating', 0, 3),
                                  replace_int_output_zero)
    pd.testing.assert_frame_equal(replace_value(candy_df5, 'rating', 5, 10),
                                  replace_int_output_positive)
    pd.testing.assert_frame_equal(replace_value(candy_df6, 'rating', 80.0, 100.0),
                                  replace_float_output)