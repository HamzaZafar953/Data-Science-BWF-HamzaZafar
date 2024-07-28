# Task 13

# Program 5: Estimating Class Probabilities

# Estimate class probabilities for a new instance
probabilities = tree_clf.predict_proba([[5, 1.5]])
predicted_class = tree_clf.predict([[5, 1.5]])

print("Estimated probabilities:", probabilities)
print("Predicted class:", predicted_class)
