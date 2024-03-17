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

# make frequency plots for the categorical columns
def make_frequency_plot(data, column: str, x_title: str):
    """ Using the data, column of interest, title, and proportion, returns a frequency plot"""
    frequency_plot = alt.Chart(data, width=280, height=200
                     ).mark_bar(size=13
                     ).encode(
                         x=alt.X(column, title=x_title),
                         y=alt.Y("count()", title="Number of Flights"),
                         tooltip=alt.Tooltip("count()")
                         )
    return frequency_plot
    
# main
def main():
    """ Loads the train and test datasets, performs the EDA, and returns the visualizations"""
    # read data
    train_data = read('../data/processed/01_flight-train.csv')

    # data table preview
    train_data_preview_path = "../results/eda_01_tbl_training-data-preview.csv"
    train_data.head().to_csv(train_data_preview_path, index=False)
    print(f"Preview of Train Dataset saved at: {train_data_preview_path}")

    # data info
    print("Data Info:")
    print(train_data.info())
    print("\n")

    # histograms for numeric columns
    print("Histograms of Numeric Columns:")
    numeric_columns = ['CONCURRENT_FLIGHTS', 'FLT_ATTENDANTS_PER_PASS',
                    'GROUND_SERV_PER_PASS', 'PLANE_AGE', 'SNOW', 'AWND']
    histogram_titles = ["Number of Concurrent Flights From the Same Departure Block", "Number of Flight Attendents per Passenger",
                    "Number of Ground Service Employees per Passenger", "Plane Age (years)", "Snowfall on Departure Day (inches)",
                    "Maximum wind speed on departure day (miles/hr)"]
    
    for column, title in zip(numeric_columns, histogram_titles):
        histogram = make_histogram(train_data, column, title)
        histogram.save(f"../results/eda_02_fig_numeric-columns-histograms_{column}.png")  # Save histogram as an image
        print(f"Histogram for {column} saved at: ../results/eda_02_fig_numeric-columns-histograms_{column}.png")
    print("\n")

    # frequency plots for categorical columns
    print("Frequency Plots of Categorical Columns:")
    frequency_plots = []
    categorical_columns = ['MONTH', 'DAY_OF_WEEK', 'CARRIER_NAME', 'DEP_DEL15']
    categorical_titles = ["Month", "Day of the Week", "Air Carrier", "Flight Departure Delay (0 = no, 1 = yes)"]
    
    for column, title in zip(categorical_columns, categorical_titles):
        frequency_plot = make_frequency_plot(train_data, column, title)
        frequency_plot.save(f"../results/eda_03_fig_categorical-columns-plots_{column}.png")  # Save frequency plot as an image
        print(f"Frequency plot for {column} saved at: ../results/eda_03_fig_categorical-columns-plots_{column}.png")
    print("\n")

if __name__ == "__main__":
    main()