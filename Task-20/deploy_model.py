# Task 20

from azureml.core.model import InferenceConfig, Model
from azureml.core.webservice import AciWebservice

# Define the inference configuration

inference_config = InferenceConfig(entry_script=script_file_name, environment=best_run.get_environment())

# Define ACI deployment configuration

aciconfig = AciWebservice.deploy_configuration(cpu_cores=1,
                                               memory_gb=1,
                                               tags={'type': "automl-heart-failure-prediction"},
                                               description='Sample service for AutoML Heart Failure Prediction')

# Deploy the model as a web service

aci_service_name = 'automl-hf-sdk'
aci_service = Model.deploy(ws, aci_service_name, [model], inference_config, aciconfig)
aci_service.wait_for_deployment(True)

# Print the deployment state

print(aci_service.state)
