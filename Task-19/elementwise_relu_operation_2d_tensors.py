# Task 19

import numpy as np

def naive_relu(x):
    assert len(x.shape) == 2  # Ensure x is a 2D tensor
    x = x.copy()  # Avoid modifying the input tensor directly
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] = max(x[i, j], 0)  # Apply ReLU
    return x

# Example usage:

x = np.array([[1, -2, 3], [-1, 5, -6], [7, -8, 9]])
output = naive_relu(x)
print(output)
