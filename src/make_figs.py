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

def plot4(data):
    alt.data_transformers.disable_max_rows()

    # Remove 'index' from id_vars
    melt_flight_predict = data.melt(id_vars=['MONTH', 'DAY_OF_WEEK', 'DEP_DEL15', 'CARRIER_NAME', 'prediction'])

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
