# Task 19

import numpy as np

def naive_add(x, y):
    assert len(x.shape) == 2  # Ensure x is a 2D tensor
    assert x.shape == y.shape  # Ensure x and y have the same shape
    x = x.copy()  # Avoid modifying the input tensor directly
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]  # Perform addition
    return x

# Example usage:

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
output = naive_add(x, y)
print(output)
