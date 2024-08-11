# Task 19

import numpy as np

def naive_add_matrix_and_vector(x, y):
    assert len(x.shape) == 2  # Ensure x is a 2D tensor
    assert len(y.shape) == 1  # Ensure y is a 1D tensor (vector)
    assert x.shape[1] == y.shape[0]  # Ensure the shapes are compatible
    x = x.copy()  # Avoid modifying the input tensor directly
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[j]  # Broadcast and add the vector to each row of the matrix
    return x

# Example usage:

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([10, 20, 30])
output = naive_add_matrix_and_vector(x, y)
print(output)
