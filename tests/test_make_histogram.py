import pandas as pd
import altair as alt
import pytest
import sys
import os

# Import make_histogram function from src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.make_histogram import make_histogram

# Test data
flight_df = pd.DataFrame({'flight':['waffle', 'ramen', 'ramen', 'wine', 'wine', 'wine', 'beer', 'pie']})
empty_df = pd.DataFrame({'flight':[]})
wrong_input = ['waffle', 'ramen', 'ramen', 'wine', 'wine', 'wine', 'beer', 'pie']

# Test for correct error handling for incorrect input type
def test_make_histogram_type_error():
    with pytest.raises(TypeError):
        make_histogram(wrong_input, 'flight', 'x-title')
        make_histogram(flight_df, 30, 'x-title')
        make_histogram(flight_df, 'flight', 30)
        make_histogram(flight_df, 'flight', 'x-title', w='width')
        make_histogram(flight_df, 'flight', 'x-title', h='height')

# Test for correct error handling if the specifed column is not in the inputted panda DataFrame
def test_make_histogram_exception():
    with pytest.raises(Exception):
        make_histogram(flight_df, 'not a column', 'x-title')
        make_histogram(empty_df, 'not a column', 'x-title')

# Test for correct return type
def test_make_histogram_returns_altair_chart():
    result = make_histogram(flight_df, 'flight', 'x-title')
    assert isinstance(result, alt.vegalite.v5.api.Chart), "make_histogram should return an altair chart"

# Test object attributes
# note: axis encoding is inaccessible, get <altair.utils.schemapi._PropertySetter at 0x16eee266550>
def test_make_histogram_attributes():
    flight_histogram = make_histogram(flight_df, 'flight', "x-title", w=300, h=400)
    assert flight_histogram.mark == 'bar', 'mark should be a bar'
    assert flight_histogram.width == 300, 'width should be 300'
    assert flight_histogram.height == 400, 'height should be 400'