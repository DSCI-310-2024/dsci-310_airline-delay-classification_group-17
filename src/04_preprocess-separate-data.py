import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from delay_finder.replace_value import replace_value
from delay_finder.read import read

def preprocess(train_file, test_file):
    """
    Preprocesses the training and test data for flight delay prediction.

    Parameters:
    train_file (str): Path to the training data CSV file.
    test_file (str): Path to the test data CSV file.

    Returns:
    None
    """
    # Read the data
    flight_train = read(train_file)
    flight_test = read(test_file)
    
    # Replace Sunday's value with 8
    replace_value(flight_train, 'DAY_OF_WEEK', 1, 8)
    replace_value(flight_test, 'DAY_OF_WEEK', 1, 8)
    
    # Save the splits
    flight_train.to_csv("data/processed/02_flight-train.csv", index=False)
    flight_test.to_csv("data/processed/02_flight-test.csv", index=False)

    # Separate feature vectors and target variables
    X_train = flight_train.drop(columns=["DEP_DEL15"])
    y_train = flight_train["DEP_DEL15"]
    X_test = flight_test.drop(columns=["DEP_DEL15"])
    y_test = flight_test["DEP_DEL15"]

    # Define transformers for preprocessing
    numeric_features = ['MONTH', 'DAY_OF_WEEK', 'CONCURRENT_FLIGHTS', 'FLT_ATTENDANTS_PER_PASS',
                        'GROUND_SERV_PER_PASS', 'PLANE_AGE', 'SNOW', 'AWND']
    numeric_transformer = StandardScaler()

    categorical_features = ['CARRIER_NAME']
    categorical_transformer = OneHotEncoder(sparse_output=False, dtype='int')

    preprocessor = make_column_transformer(
        (numeric_transformer, numeric_features),
        (categorical_transformer, categorical_features),
        remainder='passthrough'
    )

    # Fit & transform data
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)

    # Save preprocessed data
    pd.DataFrame(
