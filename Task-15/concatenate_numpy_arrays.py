# Task 15

import numpy as np

# Create two 2D arrays
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])

print("Array 1:\n", array1)
print("Array 2:\n", array2)

# Concatenate along the first axis (rows)
concatenated_array = np.concatenate((array1, array2), axis=0)
print("Concatenated Array (along rows):\n", concatenated_array)

# Concatenate along the second axis (columns)
concatenated_array = np.concatenate((array1, array2), axis=1)
print("Concatenated Array (along columns):\n", concatenated_array)
