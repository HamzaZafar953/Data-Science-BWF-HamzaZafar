# Task 20

from azureml.train.automl import AutoMLConfig

# Define the project folder

project_folder = './aml-project'

# Define AutoML settings

automl_settings = {
    "experiment_timeout_minutes": 20,
    "max_concurrent_iterations": 3,
    "primary_metric": 'AUC_weighted'
}

# Create AutoML configuration

automl_config = AutoMLConfig(compute_target=compute_target,
                             task="classification",
                             training_data=dataset,
                             label_column_name="DEATH_EVENT",
                             path=project_folder,
                             enable_early_stopping=True,
                             featurization='auto',
                             debug_log="automl_errors.log",
                             **automl_settings
                            )
