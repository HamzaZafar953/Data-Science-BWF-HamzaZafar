# Task 10 

# Iris Dataset 

import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])

# Print summary information
print(iris_df.info())
