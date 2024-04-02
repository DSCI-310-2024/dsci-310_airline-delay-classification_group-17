import pandas as pd
import pytest
import sys
import os

# Import replace_value function from src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.replace_value import replace_value

# Test data
candy_df = pd.DataFrame({'candy':['candy corn', 'smarties', 'kitkat', 'coffee crisp'], 'rating':[-5, 0, 5, 80.0]})
empty_df = pd.DataFrame({'candy':[], 'rating':[]})
wrong_input = ['candy corn', 'smarties', 'kitkat', 'coffee crisp']

# Expected outputs
replace_str_output_candy_corn = pd.DataFrame({'candy':['dirt', 'smarties', 'kitkat', 'coffee crisp'], 'rating':[-5, 0, 5, 80.0]})
replace_str_output_kitkat = pd.DataFrame({'candy':['candy corn', 'smarties', 'gold', 'coffee crisp'], 'rating':[-5, 0, 5, 80.0]})
replace_int_output_negative = pd.DataFrame({'candy':['dirt', 'smarties', 'kitkat', 'coffee crisp'], 'rating':[-10, 0, 5, 80.0]})
replace_int_output_zero = pd.DataFrame({'candy':['dirt', 'smarties', 'kitkat', 'coffee crisp'], 'rating':[-5, 3, 5, 80.0]})
replace_int_output_positive = pd.DataFrame({'candy':['dirt', 'smarties', 'kitkat', 'coffee crisp'], 'rating':[-5, 0, 10, 80.0]})
replace_float_output = pd.DataFrame({'candy':['dirt', 'smarties', 'kitkat', 'coffee crisp'], 'rating':[-5, 0, 5, 100.0]})

# Test for correct error handling for incorrect input type


# Test for correct error handling if the specifed column is not in the inputted panda DataFrame


# Test for correct error handling if the old_value is not in the specified column


# Test for correct return type


# Test if the function successfully replaces the old value in the specified column with the specified new value

