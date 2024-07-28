# Task 14

import numpy as np
import matplotlib.pyplot as plt

# Generating random linear data
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Adding x0 = 1 to each instance
X_b = np.c_[np.ones((100, 1)), X]

# Stochastic Gradient Descent parameters
n_epochs = 50
t0, t1 = 5, 50

# Learning schedule function
def learning_schedule(t):
    return t0 / (t + t1)

# Initializing theta randomly
theta = np.random.randn(2, 1)

# Stochastic Gradient Descent implementation
for epoch in range(n_epochs):
    for i in range(m):
        random_index = np.random.randint(m)
        xi = X_b[random_index:random_index + 1]
        yi = y[random_index:random_index + 1]
        gradients = 2 * xi.T.dot(xi.dot(theta) - yi)
        eta = learning_schedule(epoch * m + i)
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
