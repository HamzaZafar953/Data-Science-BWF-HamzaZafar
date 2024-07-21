# Task 12

from sklearn.metrics import precision_score, recall_score, f1_score

# Example data (replace with actual data)
y_train_5 = [0, 1, 1, 0, 1, 1, 0, 1, 0, 0]
y_train_pred = [0, 1, 1, 0, 0, 1, 0, 1, 1, 0]

# Compute precision and recall
precision = precision_score(y_train_5, y_train_pred)
recall = recall_score(y_train_5, y_train_pred)
f1 = f1_score(y_train_5, y_train_pred)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
