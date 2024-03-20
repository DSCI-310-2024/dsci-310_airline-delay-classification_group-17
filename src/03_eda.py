import pandas as pd
import altair as alt



# read data from csv file
def read(file_name):
    return pd.read_csv(file_name)

# make histograms for the numeric columns
def make_histogram(data, column: str, x_title: str, w=250, h=150):
    """ Using the data, column of interest, title, and proportion, returns a histogram"""
    numeric_plot = alt.Chart(data, width=w, height=h
              ).mark_bar(
              ).encode(
                  x=alt.X(column, title=x_title, bin=alt.Bin(maxbins=30)),
                  y=alt.Y("count()", title="Number of Flights")
                  )
    return numeric_plot

# main
def main():
    """ Loads the train and test datasets, performs the EDA, and returns the visualizations"""
    # read data
    train_data = read('../data/processed/02_flight-train.csv')

    # data table preview
    train_data_preview_path = "../results/eda_01_tbl_training-data-preview.csv"
    train_data.head().to_csv(train_data_preview_path, index=False)
    print(f"Preview of Train Dataset saved at: {train_data_preview_path}")

    # histograms for numeric columns
    ## make a list of the numeric columns in the dataset
    numeric_columns = ['CONCURRENT_FLIGHTS', 'FLT_ATTENDANTS_PER_PASS',
                        'GROUND_SERV_PER_PASS', 'PLANE_AGE', 'SNOW', 'AWND']

    ## list of titles for each histogram
    histogram_titles = ["Number of Concurrent Flights From the Same Departure Block", "Number of Flight Attendents per Passenger", 
                        "Number of Ground Service Employees per Passenger", "Plane Age (years)", "Snowfall on Departure Day (inches)",
                        "Maximum wind speed on departure day (miles/hr)"]

    ## make histograms for each numeric column
    numeric_plots = [] # accumulates the numeric plots made so far
    for x in range(len(numeric_columns)):
        numeric_plots.append(make_histogram(train_data, numeric_columns[x-1], histogram_titles[x-1]))
    
    ## save histograms as one figure
    alt.data_transformers.disable_max_rows()
    numeric_histogram = ((numeric_plots[0] | numeric_plots[1]
    ) & (numeric_plots[2] | numeric_plots[3]
        ) & (numeric_plots[4] | numeric_plots[5]))
    numeric_histogram.save('../results/eda_02_fig_numeric-columns-histograms.png')

    # frequency plots for categorical columns
    month_plot = alt.Chart(train_data, width = 280, height = 200
                        ).mark_bar(size=13
                        ).encode(
                            x = alt.X("MONTH", title = "Month"),
                            y = alt.Y("count()", title = "Number of Flights"),
                            tooltip = alt.Tooltip("count()")
                            )

    day_of_week_plot  = alt.Chart(train_data, width = 280, height = 200
                        ).mark_bar(size = 13
                        ).encode(
                            x = alt.X("DAY_OF_WEEK", title = "Day of the Week"),
                            y = alt.Y("count()", title = "Number of Flights"),
                            tooltip = alt.Tooltip("count()")
                            )

    carrier_plot  = alt.Chart(train_data, width = 400, height = 200
                        ).mark_bar(
                        ).encode(
                            x = alt.X("CARRIER_NAME", title = "Air Carrier"),
                            y = alt.Y("count()", title = "Number of Flights"),
                            tooltip = alt.Tooltip("count()")
                            )

    delay_plot  = alt.Chart(train_data, width = 100, height = 200
                        ).mark_bar(size = 20
                        ).encode(
                            x = alt.X("DEP_DEL15", title = "Flight Departure Delay (0 = no, 1 = yes)"),
                            y = alt.Y("count()", title = "Number of Flights"),
                            tooltip = alt.Tooltip("count()")
                            )

    ## save frequency charts as one figure
    freq_charts = ((month_plot | day_of_week_plot) & (carrier_plot | delay_plot))
    freq_charts.save('../results/eda_03_fig_categorical-columns-plots.png')

if __name__ == "__main__":
    main()