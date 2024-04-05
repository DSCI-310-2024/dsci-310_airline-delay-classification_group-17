import os
import sys
import pytest
import pandas as pd

# Import make_histogram function from src folder
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.make-figs import plot_chart
from src.08-make-figs import plot4

# Mock data for testing
data = pd.DataFrame({
    "MONTH": [1, 2, 3],
    "DAY_OF_WEEK": [2, 3, 4],
    "CARRIER_NAME": ["A", "B", "C"],
    "DEP_DEL15": [0, 1, 1],
    "prediction": [0, 1, 0]
})

@pytest.mark.parametrize("x_field, title, prediction_field, actual_field, save_path", [
    ("MONTH", "Month and Predicted Flight Delay", "prediction", "DEP_DEL15", "test_results/04_fig_month-vs-prediction-actual.png"),
    ("DAY_OF_WEEK", "Day of the Week and Predicted Flight Delay", "prediction", "DEP_DEL15", "test_results/05_fig_day-vs-prediction-actual.png"),
    ("CARRIER_NAME", "Flight Carriers and Predicted Flight Delay", "prediction", "DEP_DEL15", "test_results/06_fig_carrier-vs-prediction-actual.png")
])
def test_plot_chart(x_field, title, prediction_field, actual_field, save_path):
    plot_chart(data, x_field, title, prediction_field, actual_field, save_path)
    assert os.path.exists(save_path)

def test_plot4():
    # Call plot4 function
    plot4(data)

    # Check if the HTML file was generated
    assert os.path.exists("test_results/07_fig_numeric-feats-interactive-viz.html")
