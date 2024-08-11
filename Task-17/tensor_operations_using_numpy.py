# Task 17

import numpy as np

# Scalar (0D tensor)

scalar = np.array(12)
print(f'Scalar tensor: {scalar}, ndim: {scalar.ndim}')

# Vector (1D tensor)

vector = np.array([12, 3, 6, 14])
print(f'Vector tensor: {vector}, ndim: {vector.ndim}')

# Matrix (2D tensor)

matrix = np.array([[5, 78, 2, 34], [6, 79, 3, 35]])
print(f'Matrix tensor:\n{matrix}, ndim: {matrix.ndim}')

# 3D Tensor

tensor_3d = np.array([[[5, 78, 2, 34], [6, 79, 3, 35]], [[7, 80, 4, 36], [8, 81, 5, 37]]])
print(f'3D tensor:\n{tensor_3d}, ndim: {tensor_3d.ndim}')
