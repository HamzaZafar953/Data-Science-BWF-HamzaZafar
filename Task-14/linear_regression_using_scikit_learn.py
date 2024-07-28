# Task 14

import numpy as np
from sklearn.linear_model import LinearRegression

# Generating random linear data
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Performing linear regression using Scikit-Learn
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Making predictions
X_new = np.array([[0], [2]])
y_predict = lin_reg.predict(X_new)

# Plotting the model predictions
plt.plot(X_new, y_predict, "r-")
plt.plot(X, y, "b.")
plt.axis([0, 2, 0, 15])
plt.show()

print("Intercept and Coefficients:", lin_reg.intercept_, lin_reg.coef_)
