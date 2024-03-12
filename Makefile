# Makefile
# Stephanie Ta
# March 2024

# This driver script:
# - carries out the analysis of flight data
# - makes and assesses a knn model to predict flight delays
# - makes figures to analyze the knn model predictions
# This script takes no arguments.

# example usages:
# make clean
# make all

# process the data
dats : data/processed/01_filtered-data.csv \
data/processed/02_flight-train.csv \
data/processed/02_flight-test.csv \
data/processed/03_X-train.csv \
data/processed/03_y-train.csv \
data/processed/03_X-test.csv \
data/processed/03_y-test.csv \

data/processed/01_filtered-data.csv :
data/processed/02_flight-train.csv :
data/processed/02_flight-test.csv :
data/processed/03_X-train.csv :
data/processed/03_y-train.csv :
data/processed/03_X-test.csv :
data/processed/03_y-test.csv :

# make eda plots
eda : results/eda_01_tbl_training-data-preview \
results/eda_02_fig_numeric-columns-histograms.png \
results/eda_02_fig_categorical-columns-plots.png \

results/eda_01_tbl_training-data-preview :
results/eda_02_fig_numeric-columns-histograms.png :
results/eda_02_fig_categorical-columns-plots.png :

# create the models
models: results/01_baseline-model.pickle \
results/02_best-knn-model.pickle

results/01_baseline-model.pickle :
results/02_best-knn-model.pickle :

# get predictions and accuracy of the knn model
results/03_knn-test-predict.csv :

# create the results plots
plots : results/04_fig_month-vs-prediction-actual.png \
results/05_fig_day-vs-prediction-actual.png \
results/06_fig_carrier-vs-prediction-actual.png \
results/07_fig_numeric-feats-interactive-viz \

results/04_fig_month-vs-prediction-actual.png :
results/05_fig_day-vs-prediction-actual.png :
results/06_fig_carrier-vs-prediction-actual.png :
results/07_fig_numeric-feats-interactive-viz :

