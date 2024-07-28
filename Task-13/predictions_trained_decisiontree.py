# Task 13

# Program 2: Making Predictions with the Trained Decision Tree

# Use the trained tree to make predictions
predictions = tree_clf.predict([[5, 1.5]])
probabilities = tree_clf.predict_proba([[5, 1.5]])

print("Predicted class:", predictions)
print("Predicted probabilities:", probabilities)
