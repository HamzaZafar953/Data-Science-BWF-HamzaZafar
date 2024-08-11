# Task 16

import numpy as np

# Pre-process data for training the SVM model

training_X = np.vstack((X, y)).T
training_y = [0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1]

# Print the preprocessed data

print("Training Data (X):\n", training_X)
print("Training Labels (y):\n", training_y)
