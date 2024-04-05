import altair as alt
import altair as alt
import pandas as pd
import numpy as np
import sklearn

from sklearn.metrics import  confusion_matrix, ConfusionMatrixDisplay, classification_report

def plot_chart(data, x_field, title, prediction_field, actual_field, save_path):
    prediction_chart = alt.Chart(data, width=300, height=200, title=title).mark_bar().encode(
                            x=alt.X(x_field, title=x_field, axis=alt.Axis(labelAngle=0)),
                            xOffset=prediction_field,
                            y=alt.Y("count()", title="Number of Flights"),
                            color=alt.Color(prediction_field, title="Model Prediction"),
                            tooltip=alt.Tooltip(["count()", x_field])
                        )

    actual_chart = alt.Chart(data, width=300, height=200, title=title).mark_bar().encode(
                        x=alt.X(x_field, title=x_field, axis=alt.Axis(labelAngle=0)),
                        xOffset=actual_field,
                        y=alt.Y("count()", title="Number of Flights"),
                        color=alt.Color(actual_field, title="Actual"),
                        tooltip=alt.Tooltip(["count()", x_field])
                    )

    plt = (prediction_chart | actual_chart).resolve_scale(color='independent')
    plt.save(save_path)
