# Task 20

# Define model details

model_name = best_run.properties['model_name']
script_file_name = 'inference/score.py'

# Download the scoring file

best_run.download_file('outputs/scoring_file_v_1_0_0.py', 'inference/score.py')

# Register the model

description = "aml heart failure project sdk"
model = best_run.register_model(model_name=model_name,
                                model_path='./outputs/',
                                description=description,
                                tags=None)
