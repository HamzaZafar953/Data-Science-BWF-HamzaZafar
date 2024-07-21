# Task 12

from sklearn.linear_model import SGDClassifier
import numpy as np

# Example data (replace with actual data and model)
some_digit = [0.5, 1.0, 1.5, 2.0]
sgd_clf = SGDClassifier()
sgd_clf.fit([[0.5, 1.0], [1.5, 2.0], [0.5, 2.0]], [0, 1, 0])

# Compute decision scores
y_scores = sgd_clf.decision_function([some_digit])
print(f"Decision score: {y_scores}")

# Set threshold and make predictions
threshold = 0
y_some_digit_pred = (y_scores > threshold)
print(f"Prediction with threshold {threshold}: {y_some_digit_pred}")

threshold = 8000
y_some_digit_pred = (y_scores > threshold)
print(f"Prediction with threshold {threshold}: {y_some_digit_pred}")
