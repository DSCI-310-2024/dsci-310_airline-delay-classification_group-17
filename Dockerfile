# Dockerfile

# Use Python image as the base image
FROM quay.io/jupyter/scipy-notebook:2024-02-24

USER root

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN conda install -y \
    altair=5.2.0 \
    altair_saver=0.5.0 \
    conda=23.11.0 \
    jupyterlab=4.0.10 \
    matplotlib=3.8.2 \
    nb_conda_kernels=2.3.1 \
    numpy=1.26.4 \
    pandas=2.2.0 \
    python=3.11.5 \
    pytest=8.1.1 \
    scikit-learn=1.4.0 \
    tabulate=0.9.0 \
    vl-convert-python=1.3.0 \
    quarto=1.4.550

RUN pip install wheel

RUN apt-get update