# Task 15

import numpy as np

# Create a 2D array
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("Original Array:\n", array)

# Split the array into 3 sub-arrays along the first axis (rows)
split_array = np.array_split(array, 3, axis=0)
print("Split Arrays (along rows):")
for i, sub_array in enumerate(split_array):
    print(f"Sub-array {i}:\n", sub_array)

# Split the array into 2 sub-arrays along the second axis (columns)
split_array = np.array_split(array, 2, axis=1)
print("Split Arrays (along columns):")
for i, sub_array in enumerate(split_array):
    print(f"Sub-array {i}:\n", sub_array)
