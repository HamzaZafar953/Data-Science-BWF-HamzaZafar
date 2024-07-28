# Task 13

# Program 3: Training a Regression Tree

import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt

# Generate a noisy quadratic dataset
np.random.seed(42)
m = 200
X = np.random.rand(m, 1)
y = 4 * (X - 0.5) ** 2
y = y + np.random.randn(m, 1) / 10

# Train a Decision Tree Regressor
tree_reg = DecisionTreeRegressor(max_depth=2)
tree_reg.fit(X, y)

# Plot the results
X_grid = np.linspace(0, 1, 500).reshape(-1, 1)
y_pred = tree_reg.predict(X_grid)

plt.scatter(X, y, color='red')
plt.plot(X_grid, y_pred, color='blue')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Decision Tree Regression')
plt.show()
