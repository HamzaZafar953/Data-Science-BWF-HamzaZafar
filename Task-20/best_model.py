# Task 20

# Get the best run and the corresponding fitted model

best_run, fitted_model = remote_run.get_output()

# Print the parameters used for the best model

print(fitted_model)

# Print the properties of the best model

best_run.get_properties()
