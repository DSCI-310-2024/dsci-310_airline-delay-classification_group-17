import pandas as pd

# function to read data from a csv file
def read(file_name):
    return pd.read_csv(file_name)

# function to filter columns
def filter_columns(data, columns_of_interest):
    return data[columns_of_interest]

# main function
def main():
    """Read and filter full_data_flightdelay.csv for columns of interest and target, and return a csv file of filtered data"""
    # define the list of features and target columns
    list_of_features_and_target = ['MONTH', 'DAY_OF_WEEK', 'DEP_DEL15', 'CONCURRENT_FLIGHTS', 'CARRIER_NAME',
                                   'FLT_ATTENDANTS_PER_PASS', 'GROUND_SERV_PER_PASS', 'PLANE_AGE', 'SNOW', 'AWND']

    # read data from the CSV file
    raw_data = read('data/raw/full_data_flightdelay.csv')

    # filter the columns of interest
    filtered_data = filter_columns(raw_data, list_of_features_and_target)

    # sample 20,000 observations from the filtered data set
    filtered_data_sample = filtered_data.sample(n=20000, random_state=12)

    # save the filtered data set
    filtered_data_sample.to_csv("data/processed/01_filtered-data.csv", index=False)

if __name__ == "__main__":
    main()