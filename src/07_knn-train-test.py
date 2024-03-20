import pandas as pd
import numpy as np
import sklearn
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import  confusion_matrix, ConfusionMatrixDisplay, classification_report


import pickle

def main():

	X_train = pd.read_csv("data/processed/03_X-train.csv")
	y_train = pd.read_csv("data/processed/03_y-train.csv")
	X_test = pd.read_csv("data/processed/03_X-test.csv")
	y_test = pd.read_csv("data/processed/03_y-test.csv")
	
	
	best_model = pickle.load(open('results/02_best-knn-model.pickle', 'rb'))	

	best_model.fit(X_train, y_train.values.ravel())

	prediction = best_model.predict(X_test)
	
	test_score = best_model.score(X_test, y_test)
	
	test_score
	
	prediction_df = pd.DataFrame(prediction)
	prediction_df = prediction_df.rename(columns={prediction_df.columns[0]:'prediction'})

	prediction_df.to_csv("results/03_knn-test-predict.csv")

if __name__ == "__main__":
    main()

	


	
