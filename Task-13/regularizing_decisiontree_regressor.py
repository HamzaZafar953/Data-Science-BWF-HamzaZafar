# Task 13

# Program 4: Regularizing a Decision Tree Regressor

# Train a regularized Decision Tree Regressor
tree_reg = DecisionTreeRegressor(max_depth=2, min_samples_leaf=10)
tree_reg.fit(X, y)

# Plot the results
y_pred = tree_reg.predict(X_grid)

plt.scatter(X, y, color='red')
plt.plot(X_grid, y_pred, color='blue')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Regularized Decision Tree Regression')
plt.show()
