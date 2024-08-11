# Task 20

from azureml.core import Experiment

# Create an experiment

experiment_name = 'aml-experiment'
experiment = Experiment(ws, experiment_name)
