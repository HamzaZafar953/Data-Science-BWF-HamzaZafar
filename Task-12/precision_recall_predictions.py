# Task 12

import numpy as np
from sklearn.metrics import precision_score, recall_score

# Assuming y_scores and y_train_5 are already defined
# y_scores = [...]
# y_train_5 = [...]

# Define thresholds and precision values
thresholds = np.linspace(0, 10000, 1000) # Example thresholds
precisions = np.random.rand(1000) # Example precision values for demonstration

# Finding the threshold for 90% precision
threshold_90_precision = thresholds[np.argmax(precisions >= 0.90)]  # ~7816
y_train_pred_90 = (y_scores >= threshold_90_precision)

# Calculating precision and recall
precision = precision_score(y_train_5, y_train_pred_90)
recall = recall_score(y_train_5, y_train_pred_90)

print(f"Threshold for 90% precision: {threshold_90_precision}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
