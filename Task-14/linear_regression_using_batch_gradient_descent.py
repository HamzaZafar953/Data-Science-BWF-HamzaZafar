# Task 14

import numpy as np
import matplotlib.pyplot as plt

# Generating random linear data
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Adding x0 = 1 to each instance
X_b = np.c_[np.ones((100, 1)), X]

# Batch Gradient Descent parameters
eta = 0.1
n_iterations = 1000
m = 100

# Initializing theta randomly
theta = np.random.randn(2, 1)

# Batch Gradient Descent implementation
for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - eta * gradients

# Making predictions using theta
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta)

# Plotting the model predictions
plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()

print("Theta values:", theta)
