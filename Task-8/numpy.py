# Task 08

# Program 14: numpy library

# Import the numpy library
import numpy as np

# Create a 1D array
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(array_1d)

# Create a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n2D Array:")
print(array_2d)

# Perform element-wise addition
added_array = array_1d + 10
print("\nArray after adding 10 to each element:")
print(added_array)

# Perform element-wise multiplication
multiplied_array = array_1d * 2
print("\nArray after multiplying each element by 2:")
print(multiplied_array)

# Compute the mean of the 2D array
mean_value = np.mean(array_2d)
print("\nMean of 2D array:")
print(mean_value)

# Compute the sum of the 2D array
sum_value = np.sum(array_2d)
print("\nSum of 2D array:")
print(sum_value)

# Compute the standard deviation of the 2D array
std_value = np.std(array_2d)
print("\nStandard deviation of 2D array:")
print(std_value)

# Create an array of zeros
zeros_array = np.zeros((3, 3))
print("\n3x3 Array of zeros:")
print(zeros_array)

# Create an array of ones
ones_array = np.ones((2, 4))
print("\n2x4 Array of ones:")
print(ones_array)

# Create an identity matrix
identity_matrix = np.eye(3)
print("\n3x3 Identity matrix:")
print(identity_matrix)

# Reshape a 1D array to a 2D array
reshaped_array = np.reshape(array_1d, (1, 5))
print("\nReshaped 1D array to 2D array:")
print(reshaped_array)
