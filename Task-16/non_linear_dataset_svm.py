# Task 16

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn import svm

# Create non-linear data

circle_X, circle_y = datasets.make_circles(n_samples=300, noise=0.05)

# Plot the non-linear data

plt.scatter(circle_X[:, 0], circle_X[:, 1], c=circle_y, marker='.')
plt.show()
