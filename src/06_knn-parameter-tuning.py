import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
import pickle

def main():
    """
    Trains a K-Nearest Neighbors (KNN) classifier and saves the best model to a pickle file.

    Reads preprocessed training data, trains KNN models with varying numbers of neighbors,
    selects the best model based on cross-validation scores, and saves it to a file.

    Returns:
    None
    """
    # Read preprocessed data
    y_train = pd.read_csv("data/processed/03_y-train.csv")
    X_train = pd.read_csv("data/processed/03_X-train.csv")

    # Dictionary to store results
    results_dict = {
        "n_neighbors": [],
        "mean_train_score": [],
        "mean_cv_score": []
    }

    # Loop over different values of n_neighbors
    for n in range(10, 41, 2):
        # Initialize KNN model
        knn_model = KNeighborsClassifier(n_neighbors=n)
        # Perform cross-validation
        cv_scores = cross_validate(knn_model, X_train, y_train.values.ravel(), cv=5, return_train_score=True)
        # Update results dictionary
        results_dict["n_neighbors"].append(n)
        results_dict["mean_train_score"].append(cv_scores["train_score"].mean())
        results_dict["mean_cv_score"].append(cv_scores["test_score"].mean())

    # Convert results dictionary to DataFrame
    results_df = pd.DataFrame(results_dict)

    # Select best value of n_neighbors
    best_k = int(results_df.loc[results_df['mean_cv_score'].idxmax()]['n_neighbors'])
    
    # Train the best KNN model
    knn_best = KNeighborsClassifier(n_neighbors=best_k)
    knn_best.fit(X_train, y_train.values.ravel())

    # Save the best KNN model to a pickle file
    with open('results/02_best-knn-model.pickle', 'wb') as f:
        pickle.dump(knn_best, f)

if __name__ == "__main__":
    main()


