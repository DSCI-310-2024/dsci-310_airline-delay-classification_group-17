# Analysis and Prediction of Airline Delays in 2019
Authors: Siddharth Balodi, Charles Benkard, Mikel Ibarra Gallardo, and Stephanie Ta

## Summary

In this project, we delve into a 2019 airline delays dataset to dissect the intricate factors contributing to flight disruptions. Our analysis aims to address pivotal questions, such as what are the primary drivers behind flight delays and cancellations? Are certain airlines or airports more vulnerable to these disruptions? How do external factors like adverse weather conditions or air traffic congestion exacerbate flight schedules? While previous studies have touched upon aspects of flight disruptions, we endeavor to provide a deeper understanding through the lens of  analytical techniques, including descriptive statistics, data visualization, and machine learning algorithms (specifically KNN classification).

Through our exploration, we have unearthed compelling insights. We have found that airport congestion, inclement weather, and airline operational issues are key contributors to flight disruptions. Furthermore, our analysis has revealed disparities in performance among airlines and airports, shedding light on areas ripe for operational enhancements and service improvements. By leveraging these findings, stakeholders within the aviation industry can make informed decisions aimed at minimizing disruptions and enhancing overall operational efficiency.

The significance of our research extends beyond the realm of academia. By unraveling the complexities of flight disruptions, we aim to empower decision-makers with actionable insights to navigate the challenges inherent in air travel. Moreover, our findings hold the potential to drive positive change within the aviation industry, ultimately leading to a more seamless and reliable travel experience for passengers worldwide.


## How to run the data analysis
We are using a virtual environment to make our computational environment reproducible.

To replicate our analysis:

1. Clone this GitHub repository to your local machine:
    - Click the green `<> Code` button and copy the url.
    - Navigate to where you'd like the cloned repository to reside in your local machine via the terminal.
    - Run the command `git clone <url>` in the terminal.
2. Create an environment from the environment file:
    - Navigate into the cloned (local) repository by running the command `cd dsci-310_airline-delay-classification_group-17`.
    - Run the command `conda env create --file environment.yml` in the terminal.
    - Activate the environment by running the command `conda activate airline_project_env` in the terminal.
3. Open JupterLab by running the command `jupyter lab` in the terminal.
4. In the JupyterLab web application, navigate to the `reports` folder, open the file `airline-delay-classification-report.ipynb`.
5. Change the kernel in the JupyerLab web application:
    - Under the `Kernel` tab, click on `Change Kernel...`.
    - Select the `Python [conda env:airline_project_env]` option in the dropdown that pops up.
6. Run the report from top to bottom in the JupyterLab web application.


## Dependencies
Python version 3.11.5

### Python packages:
  - `altair==5.2.0`
  - `jupyterlab==4.0.10`
  - `matplotlib==3.8.2`
  - `nb_conda_kernels==2.3.1`
  - `numpy==1.26.4`
  - `pandas==2.2.0`
  - `scikit-learn==1.4.0`

## Licences

This project is licensed under the terms of the MIT License. If re-using/re-mixing please provide attribution and link to this webpage.
