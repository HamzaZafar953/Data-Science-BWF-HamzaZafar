# Task 14

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generating random linear data
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Adding x0 = 1 to each instance
X_b = np.c_[np.ones((100, 1)), X]

# Calculating theta using the Normal Equation
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Making predictions using theta
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]
y_predict = X_new_b.dot(theta_best)

# Plotting the model predictions
plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()

print("Theta best values:", theta_best)
