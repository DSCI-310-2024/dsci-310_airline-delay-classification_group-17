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
	
	
	best_model = pickle.load(open('../results/02_best-knn-model.pickle', 'rb'))	

	best_model.fit(X_train, y_train)

	prediction = best_model.predict(X_test)
	
	test_score = best_model.score(X_test, y_test)
	
	test_score
	
	prediction.to_csv("../results/03_knn-test-predict.csv")

if __name__ == "__main__":
    main()

	


	
