# Task 15

import numpy as np

# Create a 2D array
array = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

print("Original Array:\n", array)

# Horizontally split the array into 2 sub-arrays
hsplit_array = np.hsplit(array, 2)
print("Horizontally Split Arrays:")
for i, sub_array in enumerate(hsplit_array):
    print(f"Sub-array {i}:\n", sub_array)

# Horizontally split the array into 4 sub-arrays
hsplit_array = np.hsplit(array, 4)
print("Horizontally Split Arrays:")
for i, sub_array in enumerate(hsplit_array):
    print(f"Sub-array {i}:\n", sub_array)
