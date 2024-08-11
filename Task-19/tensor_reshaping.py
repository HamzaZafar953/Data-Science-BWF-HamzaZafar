# Task 19

import numpy as np

# Example usage:

x = np.array([[0., 1.], [2., 3.], [4., 5.]])
print(f"Original shape: {x.shape}")
print(x)

# Reshape to (6, 1)

x = x.reshape((6, 1))
print(f"\nReshaped to (6, 1):")
print(x)

# Reshape to (2, 3)

x = x.reshape((2, 3))
print(f"\nReshaped to (2, 3):")
print(x)
