# CS-433: Machine Learning Fall 2022, Project 1 
- Team Name: Los_Caballeros_De_Bogota
- Team Member:
    1. Lelièvre Maxime, **SCIPER: 296777** (maxime.lelievre@epfl.ch)
    2. Peduto Matteo, **SCIPER: 316194** (matteo.peduto@epfl.ch)
    3. Mery Tom, **SCIPER: 297217** (tom.mery@epfl.ch)

* [Getting started](#getting-started)
    * [Project description](#project-description)
    * [Data](#data)
    * [Report](#report)
* [Reproduce results](#reproduce-results)
    * [Requirements](#Requirements)
    * [Repo Architecture](#repo-architecture)
    * [Instructions to run](#instructions-to-run)
* [Results](#results)

# Getting started
## Project description
The aim of this project of Machine Learning is to predict if a decay signature is a Higgs Boson or some other particle.
The model is based on a vector of features of a collision event between two high speed protons. More detail about the project ara available in `references/project1_description.pdf`. Here a regularized logistic regression is implemented and trained on 8 sub-sets of the full dataset. 
## Data
The Dataset comes from a popular machine learning challenge recently - finding the Higgs boson - using original data from CERN. The dataset is available at https://www.aicrowd.com/challenges/epfl-machine-learning-higgs. To reproduce the results a folder `data/` should be added to the repo, as described in [Repo Architecture](#repo-architecture). A detailed description of the dataset is availabel in `references/The_Higgs_boson_ML_challenge.pdf`.

## Report
All the detailed about the choices that has been made and the methodology used throughout this project are available in `report.pdf`. Through this report, the reader is able to understand the different assumptions, decisions and results made during the project
# Reproduce results
## Requirements
- Python==3.9.13
- Numpy==1.21.5
- Matplotlib

## Repo Architecture
<pre>  
├─── data
    ├─── submission.csv: File generated by run.py. Contains predictions of sample from test.csv. 
    ├─── test.csv: File containing samples to be predicted.
    ├─── train.csv: File with labeled sample using for training.
├─── notebooks
    ├─── data_analysis.ipynb: Exploratory data analysis notebooks. Helps to visualize distributions of features.
    ├─── experiments.ipynb: Notebooks assessing performance of very basics models.
├─── references
    ├─── project1_description.pdf: Original description of the project provided by EPFL.
    ├─── The_Higgs_boson_ML_challenge.pdf: Reference used to understand features of the dataset.
├─── src
    ├─── __init__.py: File to define src directory as a python package
    ├─── best_params.pkl: File generated by optimization.py. Contains best degree and lambda_ for each sub-models. This file is loaded in run.py.
    ├─── data_processing.py: File containing implementations to process the raw data.
    ├─── helpers.py: File provided by EPFL containing methods to load the data and create submissions for aircrowd.
    ├─── model.py: File containing definition of the class Model
    ├─── utils.py: File containing useful function for computing and visualization purpose.
├─── implementations.py: File containing basics ML implementations asked in the project description.
├─── optimization.py: File used to optimize parameters. Performs cross-validation and saved best parameters in best_params.pkl. 
├─── README.md: README
├─── report.pdf: Report explaining choices that has been made.
└─── run.py: File that load the dataset, trains models with parameters in best_params.pkl and generate submissison.csv.
</pre>

## Instructions to run 
Move to the root folder and execute:

    python run.py

Make sure to have all the requirements and the data folder in the root. 

# Results
The performances of the models is assessed on AirCrowd from `data/submission.csv` generated by `run.py`. The model achieves a global accuracy of with a F1-score of .