# Task 16

import matplotlib.pyplot as plt
import numpy as np

# Get the weight values for the linear equation from the trained SVM model

w = clf.coef_[0]

# Get the y-offset for the linear equation

a = -w[0] / w[1]

# Make the x-axis space for the data points

XX = np.linspace(0, 13)

# Get the y-values to plot the decision boundary

yy = a * XX - clf.intercept_[0] / w[1]

# Plot the decision boundary

plt.plot(XX, yy, 'k-', label='Decision Boundary')

# Show the plot visually

plt.scatter(training_X[:, 0], training_X[:, 1], c=training_y, cmap='coolwarm')
plt.legend()
plt.show()
