import pandas as pd
from sklearn.model_selection import train_test_split

# function to read data from a csv file
def read(file_name):
    return pd.read_csv(file_name)

# main function
def main():
    """ Read filtered data set and split it into train and test states in csv form"""
    # read csv file
    filtered_data = read("../data/processed/01_filtered-data.csv")

    # split the data into train and test sets
    flight_train, flight_test = train_test_split(filtered_data, test_size=0.2, random_state=12, stratify=filtered_data["DEP_DEL15"])

    # save the train and test sets into csv files
    flight_train.to_csv("../data/processed/02_flight-train.csv", index = False)
    flight_test.to_csv("../data/processed/02_flight-test.csv", index = False)

if __name__ == "__main__":
    main()