# Task 19

import numpy as np

def naive_matrix_vector_dot(x, y):
    assert len(x.shape) == 2  # Ensure x is a 2D tensor (matrix)
    assert len(y.shape) == 1  # Ensure y is a 1D tensor (vector)
    assert x.shape[1] == y.shape[0]  # Ensure the shapes are compatible
    z = np.zeros(x.shape[0])  # Initialize the result vector with zeros
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i] += x[i, j] * y[j]  # Perform the dot product
    return z

# Example usage:

x = np.array([[1, 2], [3, 4], [5, 6]])
y = np.array([10, 20])
output = naive_matrix_vector_dot(x, y)
print(output)
