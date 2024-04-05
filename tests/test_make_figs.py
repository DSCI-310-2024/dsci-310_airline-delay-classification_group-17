import os
import sys
import pytest
import pandas as pd

# Import plot_chart and plot4 functions from make_figs module
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.make_figs import plot_chart, plot4

@pytest.fixture
def sample_data():
    data = {
        'MONTH': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'DAY_OF_WEEK': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
        'CARRIER_NAME': ['A', 'B', 'C', 'D', 'E'],
        'DEP_DEL15': [0, 1, 0, 1, 0],
        'prediction': [0, 1, 1, 0, 1],
        'index': [1, 2, 3, 4, 5]  # Adding 'index' column for the test
    }
    return pd.DataFrame(data)

@pytest.mark.parametrize("x_field, title, prediction_field, actual_field, save_path", [
    ("MONTH", "Month and Predicted Flight Delay", "prediction", "DEP_DEL15", "test_results/04_fig_month-vs-prediction-actual.svg"),
    ("DAY_OF_WEEK", "Day of the Week and Predicted Flight Delay", "prediction", "DEP_DEL15", "test_results/05_fig_day-vs-prediction-actual.svg"),
    ("CARRIER_NAME", "Flight Carriers and Predicted Flight Delay", "prediction", "DEP_DEL15", "test_results/06_fig_carrier-vs-prediction-actual.svg")
])
def test_plot_chart(x_field, title, prediction_field, actual_field, save_path, sample_data):
    plot_chart(sample_data, x_field, title, prediction_field, actual_field, save_path)
    assert os.path.exists(save_path)

def test_plot4(sample_data):
    # Call plot4 function
    plot4(sample_data)
