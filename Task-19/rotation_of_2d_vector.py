# Task 19

import numpy as np

def rotate_vector(v, theta):
    u = np.array([np.cos(theta), np.sin(theta)])
    w = np.array([-np.sin(theta), np.cos(theta)])
    R = np.array([u, w])  # Rotation matrix
    return np.dot(R, v)

# Example usage:

v = np.array([1, 0])  # Vector to rotate
theta = np.pi / 4  # 45 degrees in radians
rotated_v = rotate_vector(v, theta)
print("Original vector:", v)
print("Rotated vector:", rotated_v)
