import pandas as pd
import numpy as np
import sklearn
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_validate
import pickle

def main():
	
	y_train = pd.read_csv("../data/03_y-train.csv")
	X_train = pd.read_csv("../data/03_X-train.csv")


	results_dict = {
    		"n_neighbors": [],
    		"mean_train_score": [],
    		"mean_cv_score": []}

	for n in range(10,41, 2):
    		knn_model = KNeighborsClassifier(n_neighbors=n)
    		cv_scores = cross_validate(knn_model, X_train, y_train, cv=5, return_train_score=True)
    		results_dict["n_neighbors"].append(n)
    		results_dict["mean_train_score"].append(cv_scores["train_score"].mean())
    		results_dict["mean_cv_score"].append(cv_scores["test_score"].mean())

	results_df = pd.DataFrame(results_dict)

	results_df.sort_values(by=["mean_cv_score"], ascending=False).head(1)

	best_k = int(results_df.loc[results_df['mean_cv_score'].idxmax()]['n_neighbors'])
	
	knn_best = KNeighborsClassifier(n_neighbors=best_k)
	f = open('../results/02_best-knn-model.pickle', 'wb')
	pickle.dump(knn_best, f)


if __name__ == "__main__":
    main()


