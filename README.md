# Project Title
Authors: Siddharth Balodi, Charles Benkard, Mikel Ibarra Gallardo, and Stephanie Ta

## Summary


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
