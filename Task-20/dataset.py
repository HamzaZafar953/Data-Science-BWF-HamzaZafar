# Task 20

# Get the dataset from the workspace

dataset = ws.datasets['heart-failure-records']
df = dataset.to_pandas_dataframe()

# Display the summary of the dataset

df.describe()
