import pandas as pd
import numpy as np
import sklearn
from sklearn.dummy import DummyClassifier
from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import cross_validate
import pickle


def read(file_name):
	return pd.read_csv(file_name)

def main():
	X_train = read("../data/processed/03_X-train.csv")
	y_train = read("../data/processed/03_y-train.csv")

	scoring = {'accuracy': 'accuracy',
           'precision': make_scorer(precision_score, pos_label=1),
           'recall': make_scorer(recall_score, pos_label=1),
           'f1': make_scorer(f1_score, pos_label=1) }

	dummy_classifier = DummyClassifier(strategy = "stratified", random_state = 12)

	dummy_scores = pd.DataFrame(
    		cross_validate(
        		dummy_classifier, X_train, y_train, cv = 5, return_train_score = True, scoring = scoring
    		)
	)

	dummy_mean = dummy_scores.mean()
	
	baseline_model = dummy_classifier
	f = open('../results/01_baseline-model.pickle', 'wb')
	pickle.dump(baseline_model, f)
	
if __name__ == "__main__":
	main()


