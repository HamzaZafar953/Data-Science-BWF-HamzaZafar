# Task 20

from azureml.core.compute import AmlCompute

# Define the name for your compute cluster

aml_name = "heart-f-cluster"

try:

    # Try to get the existing cluster
    
    aml_compute = AmlCompute(ws, aml_name)
    print('Found existing AML compute context.')
    
except:

    # Create a new cluster if it doesn't exist
    
    print('Creating new AML compute context.')
    aml_config = AmlCompute.provisioning_configuration(vm_size="Standard_D2_v2", min_nodes=1, max_nodes=3)
    aml_compute = AmlCompute.create(ws, name=aml_name, provisioning_configuration=aml_config)
    aml_compute.wait_for_completion(show_output=True)

# Get the compute target

cts = ws.compute_targets
compute_target = cts[aml_name]
