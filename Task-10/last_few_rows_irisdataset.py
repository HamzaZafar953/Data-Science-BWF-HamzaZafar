# Task 10 

# Displaying Last Few Rows of Iris Dataset

import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()
iris_df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])

# Display last few rows
print(iris_df.tail())
 
