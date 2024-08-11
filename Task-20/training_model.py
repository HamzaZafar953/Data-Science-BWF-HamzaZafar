# Task 20

# Submit the experiment for training

remote_run = experiment.submit(automl_config)

# Show the RunDetails widget for tracking the experiment progress

from azureml.widgets import RunDetails
RunDetails(remote_run).show()
