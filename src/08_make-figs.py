import altair as alt
import pandas as pd
import numpy as np
import sklearn

from sklearn.metrics import  confusion_matrix, ConfusionMatrixDisplay, classification_report
from make-figs import plot_chart, plot4

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


if __name__ == "__main__":
    main
