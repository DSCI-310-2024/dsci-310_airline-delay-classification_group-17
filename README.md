# Analysis and Prediction of Airline Delays in 2019
Authors: Siddharth Balodi, Charles Benkard, Mikel Ibarra Gallardo, and Stephanie Ta

## Summary

In this project, we delve into a 2019 airline delays dataset to dissect the intricate factors contributing to flight disruptions. Our analysis aims to address pivotal questions, such as what are the primary drivers behind flight delays and cancellations? Are certain airlines or airports more vulnerable to these disruptions? How do external factors like adverse weather conditions or air traffic congestion exacerbate flight schedules? While previous studies have touched upon aspects of flight disruptions, we endeavor to provide a deeper understanding through the lens of  analytical techniques, including descriptive statistics, data visualization, and machine learning algorithms (specifically KNN classification).

Through our exploration, we have unearthed compelling insights. We have found that airport congestion, inclement weather, and airline operational issues are key contributors to flight disruptions. Furthermore, our analysis has revealed disparities in performance among airlines and airports, shedding light on areas ripe for operational enhancements and service improvements. By leveraging these findings, stakeholders within the aviation industry can make informed decisions aimed at minimizing disruptions and enhancing overall operational efficiency.

The significance of our research extends beyond the realm of academia. By unraveling the complexities of flight disruptions, we aim to empower decision-makers with actionable insights to navigate the challenges inherent in air travel. Moreover, our findings hold the potential to drive positive change within the aviation industry, ultimately leading to a more seamless and reliable travel experience for passengers worldwide.


## How to run the data analysis
We are now using a Docker container to make our computational environment reproducible.

To replicate our analysis using Docker:

1. Clone this GitHub repository to your local machine:
    - Click the green `<> Code` button and copy the url.
    - Navigate to where you'd like the cloned repository to reside in your local machine via the terminal.
    - Run the command `git clone <url>` in the terminal.
2. Open Docker Desktop.
2. To remove the results of our analysis, run the following command in the terminal:
    `docker-compose run --rm airline-analysis-env make clean-all`
5. To remake the results of the analysis, run the commands following command in the terminal:
    `docker-compose run --rm airline-analysis-env make all`
6. View the analysis report `airline-delay-classification-report.html` in the reports directory.


## Dependencies
Docker Desktop, Quarto version 1.4.550, Python version 3.11.5, and the python packages listed below.

### Python packages:
  - altair==5.2.0
  - altair_saver==0.5.0
  - conda==23.11.0
  - jupyterlab==4.0.10
  - matplotlib==3.8.2
  - nb_conda_kernels==2.3.1
  - numpy==1.26.4
  - pandas==2.2.0
  - python==3.11.5
  - pytest==8.1.1
  - scikit-learn==1.4.0
  - tabulate==0.9.0
  - vl-convert-python==1.3.0

## Licences

The code of this project is licensed under the terms of the MIT License and the aalysis report is licensed under the terms of Creative Commons 4.0 License. If re-using/re-mixing please provide attribution and link to this webpage. For more details, navigate to our [LICENSE](https://github.com/DSCI-310-2024/dsci-310_airline-delay-classification_group-17/blob/main/LICENSE).
