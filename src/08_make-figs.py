import altair as alt
import pandas as pd
import numpy as np
import sklearn

from sklearn.metrics import  confusion_matrix, ConfusionMatrixDisplay, classification_report
from make-figs import plot_chart

def main():
    predictions = pd.read_csv("results/03_knn-test-predict.csv")
    flight_test = pd.read_csv("data/processed/02_flight-test.csv").reset_index()

    flight_test_predict = pd.concat([flight_test, predictions], axis=1)

    flight_test_predict["MONTH"] = flight_test_predict["MONTH"].replace({1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun", 7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"})

    flight_test_predict["DAY_OF_WEEK"] = flight_test_predict["DAY_OF_WEEK"].replace({2: "Mon", 3: "Tue", 4: "Wed", 5: "Thu", 6: "Fri", 7: "Sat", 8: "Sun"})
    flight_test_predict["prediction"] = flight_test_predict["prediction"].replace({0: "not delayed", 1: "delayed"})
    flight_test_predict["DEP_DEL15"] = flight_test_predict["DEP_DEL15"].replace({0: "not delayed", 1: "delayed"})

    plot1(flight_test_predict)
    plot2(flight_test_predict)
    plot3(flight_test_predict)
    plot4(flight_test_predict)

def plot1(data):
    plot_chart(data, "MONTH", "Month and Predicted Flight Delay", "prediction", "DEP_DEL15", "results/04_fig_month-vs-prediction-actual.png")

def plot2(data):
    plot_chart(data, "DAY_OF_WEEK", "Day of the Week and Predicted Flight Delay", "prediction", "DEP_DEL15", "results/05_fig_day-vs-prediction-actual.png")

def plot3(data):
    plot_chart(data, "CARRIER_NAME", "Flight Carriers and Predicted Flight Delay", "prediction", "DEP_DEL15", "results/06_fig_carrier-vs-prediction-actual.png")

def plot4(data):
    alt.data_transformers.disable_max_rows()

    melt_flight_predict = data.melt(id_vars=['MONTH', 'DAY_OF_WEEK', 'DEP_DEL15', 'CARRIER_NAME', 'prediction', 'index'])

    dropdown_options = ['CONCURRENT_FLIGHTS', 'FLT_ATTENDANTS_PER_PASS', 'GROUND_SERV_PER_PASS', 'PLANE_AGE', 'SNOW', 'AWND']
    dropdown_numeric_variable = alt.binding_select(options=dropdown_options, name='Y-axis feature')
    selection = alt.selection_point(fields=['variable'], bind=dropdown_numeric_variable)

    drop_down_chart = alt.Chart(melt_flight_predict, width=1000, height=400
                                    ).mark_circle(opacity=0.4).encode(
                                        y=alt.X('value:Q', title=""),
                                        x=alt.Y('MONTH', title="Month", sort=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]),
                                        color=alt.Color('prediction', title="Model Prediction")
                                    ).add_params(selection).transform_filter(selection)

    drop_down_chart.save("results/07_fig_numeric-feats-interactive-viz.html")

if __name__ == "__main__":
    main
