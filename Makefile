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

all: 

# process the data
dats : data/processed/01_filtered-data.csv \
data/processed/02_flight-train.csv \
data/processed/02_flight-test.csv \
data/processed/03_X-train.csv \
data/processed/03_y-train.csv \
data/processed/03_X-test.csv \
data/processed/03_y-test.csv

data/processed/01_filtered-data.csv : src/01_filter-raw-data.py data/raw/full_data_flightdelay.csv
	python src/01_filter-raw-data.py
data/processed/02_flight-train.csv : src/02_split-data.py data/processed/01_filtered-data.csv
	python src/02_split-data.py
data/processed/02_flight-test.csv : src/02_split-data.py data/processed/01_filtered-data.csv
	python src/02_split-data.py
data/processed/03_X-train.csv : src/04_preprocess-separate-data.py data/processed/02_flight-train.csv
	python src/04_preprocess-separate-data.py
data/processed/03_y-train.csv : src/04_preprocess-separate-data.py data/processed/02_flight-train.csv
	python src/04_preprocess-separate-data.py
data/processed/03_X-test.csv : src/04_preprocess-separate-data.py data/processed/02_flight-test.csv
	python src/04_preprocess-separate-data.py
data/processed/03_y-test.csv :src/04_preprocess-separate-data.py data/processed/02_flight-test.csv
	python src/04_preprocess-separate-data.py

# make eda plots
eda : results/eda_01_tbl_training-data-preview \
results/eda_02_fig_numeric-columns-histograms.png \
results/eda_02_fig_categorical-columns-plots.png

results/eda_01_tbl_training-data-preview : src/03_eda.py data/processed/02_flight-train.csv
	python src/03_eda.py
results/eda_02_fig_numeric-columns-histograms.png : src/03_eda.py data/processed/02_flight-train.csv
	python src/03_eda.py
results/eda_02_fig_categorical-columns-plots.png : src/03_eda.py data/processed/02_flight-train.csv
	python src/03_eda.py

# create the models
models: results/01_baseline-model.pickle \
results/02_best-knn-model.pickle
	python 
results/01_baseline-model.pickle : src/05_baseline-model-accuracy.py \
data/processed/03_X-train.csv data/processed/03_y-train.csv
	python src/05_baseline-model-accuracy.py
results/02_best-knn-model.pickle : src/06_knn-parameter-tuning.py \
data/processed/03_X-train.csv data/processed/03_y-train.csv
	python src/05_baseline-model-accuracy.py

# get predictions and accuracy of the knn model
results/03_knn-test-predict.csv : src/07_knn-train-test.py \
data/processed/03_X-train.csv data/processed/03_y-train.csv \
results/02_best-knn-model.pickle
	python src/07_knn-train-test.py

# create the results plots
results-plots : results/04_fig_month-vs-prediction-actual.png \
results/05_fig_day-vs-prediction-actual.png \
results/06_fig_carrier-vs-prediction-actual.png \
results/07_fig_numeric-feats-interactive-viz

results/04_fig_month-vs-prediction-actual.png : src/08_make-figs.py results/03_knn-test-predict.csv
	python src/08_make-figs.py
results/05_fig_day-vs-prediction-actual.png : src/08_make-figs.py results/03_knn-test-predict.csv
	python src/08_make-figs.py
results/06_fig_carrier-vs-prediction-actual.png : src/08_make-figs.py results/03_knn-test-predict.csv
	python src/08_make-figs.py
results/07_fig_numeric-feats-interactive-viz : src/08_make-figs.py results/03_knn-test-predict.csv
	python src/08_make-figs.py

# render the report
reports/airline-delay-classification-report.html : reports/airline-delay-classification-report.qmd \
eda results-plots
	quarto render reports/airline-delay-classification-report.qmd

# clean output :
clean-dats :
	rm -f data/processed/01_filtered-data.csv \
	data/processed/02_flight-train.csv \
	data/processed/02_flight-test.csv \
	data/processed/03_X-train.csv \
	data/processed/03_y-train.csv \
	data/processed/03_X-test.csv \
	data/processed/03_y-test.csv

clean-eda :
	rm -f results/eda_01_tbl_training-data-preview \
	results/eda_02_fig_numeric-columns-histograms.png \
	results/eda_02_fig_categorical-columns-plots.png

clean-models :
	rm -f results/01_baseline-model.pickle \
	results/02_best-knn-model.pickle

clean-predictions :
	rm -f results/03_knn-test-predict.csv

clean-results-plots :
	rm -f results/04_fig_month-vs-prediction-actual.png \
	results/05_fig_day-vs-prediction-actual.png \
	results/06_fig_carrier-vs-prediction-actual.png \
	results/07_fig_numeric-feats-interactive-viz

clean-report :
	rm -f reports/airline-delay-classification-report.html
	rm -rf reports/airline-delay-classification-report_files/

clean-all : clean-dats clean-eda clean-models clean-predictions clean-results-plots clean-report