import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import make_pipeline

# read data from csv file
def read(file_name):
    return pd.read_csv(file_name)

# main
def preprocess(train_file, test_file):
    # read the data
    flight_train = read(train_file)
    flight_test = read(test_file)
    
    # replace sunday's value
    flight_train.loc[flight_train['DAY_OF_WEEK'] == 1, 'DAY_OF_WEEK'] = 8
    flight_test.loc[flight_test['DAY_OF_WEEK'] == 1, 'DAY_OF_WEEK'] = 8
    
    # save the splits after 
    flight_train.to_csv("../data/processed/02_flight-train.csv", index=False)
    flight_test.to_csv("../data/processed/02_flight-test.csv", index=False)

    # separate feature vectors
    X_train = flight_train.drop(columns=["DEP_DEL15"])
    y_train = flight_train["DEP_DEL15"]
    X_test = flight_test.drop(columns=["DEP_DEL15"])
    y_test = flight_test["DEP_DEL15"]

    # preprocess features
    numeric_features = ['MONTH', 'DAY_OF_WEEK', 'CONCURRENT_FLIGHTS', 'FLT_ATTENDANTS_PER_PASS',
                        'GROUND_SERV_PER_PASS', 'PLANE_AGE', 'SNOW', 'AWND']
    numeric_transformer = StandardScaler()

    categorical_features = ['CARRIER_NAME']
    categorical_transformer = OneHotEncoder(sparse=False, dtype='int')

    preprocessor = make_column_transformer(
        (numeric_transformer, numeric_features),
        (categorical_transformer, categorical_features),
        remainder='passthrough'
    )

    # fit & transform data
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    # save data
    pd.DataFrame(X_train).to_csv("../data/processed/03_X-train.csv", index=False)
    pd.DataFrame(y_train).to_csv("../data/processed/03_y-train.csv", index=False)
    pd.DataFrame(X_test).to_csv("../data/processed/03_X-test.csv", index=False)
    pd.DataFrame(y_test).to_csv("../data/processed/03_y-test.csv", index=False)

if __name__ == "__main__":
    preprocess_data("../data/processed/02_flight-train.csv", "../data/processed/02_flight-test.csv")
