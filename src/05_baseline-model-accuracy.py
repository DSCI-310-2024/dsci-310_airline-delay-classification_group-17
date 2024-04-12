import pandas as pd
import numpy as np
import sklearn
from sklearn.dummy import DummyClassifier
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import cross_validate
import pickle
from delay_finder.read import read

def main():
    """
    Trains a baseline model using a dummy classifier and saves the model to a pickle file.

    Reads preprocessed training data, trains the model, and saves it to a file.

    Returns:
    None
    """
    # Read preprocessed data
    X_train = read("data/processed/03_X-train.csv")
    y_train = read("data/processed/03_y-train.csv")

    # Define scoring metrics
    scoring = {'accuracy': 'accuracy',
               'precision': make_scorer(precision_score, pos_label=1),
               'recall': make_scorer(recall_score, pos_label=1),
               'f1': make_scorer(f1_score, pos_label=1)}

    # Initialize dummy classifier
    dummy_classifier = DummyClassifier(strategy="stratified", random_state=12)

    # Perform cross-validation and compute scores
    dummy_scores = pd.DataFrame(
        cross_validate(
            dummy_classifier, X_train, y_train, cv=5, return_train_score=True, scoring=scoring
        )
    )

    # Compute mean scores
    dummy_mean = dummy_scores.mean()

    # Save baseline model to a pickle file
    baseline_model = dummy_classifier
    with open('results/01_baseline-model.pickle', 'wb') as f:
        pickle.dump(baseline_model, f)

if __name__ == "__main__":
    main()
