import matplotlib.pyplot as plt
# Task 12

from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import cross_val_predict

# Example data and model (replace with actual data and model)
X_train = np.array([[0.5, 1.0], [1.5, 2.0], [0.5, 2.0], [1.0, 1.5]])
y_train_5 = np.array([0, 1, 0, 1])
sgd_clf = SGDClassifier()
sgd_clf.fit(X_train, y_train_5)

# Compute decision scores for all instances in the training set
y_scores = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3, method="decision_function")

# Compute precision and recall for all possible thresholds
precisions, recalls, thresholds = precision_recall_curve(y_train_5, y_scores)

# Plot precision and recall as functions of the threshold value
def plot_precision_recall_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
    plt.plot(thresholds, recalls[:-1], "g-", label="Recall")
    plt.xlabel("Threshold")
    plt.ylabel("Score")
    plt.legend()
    plt.grid(True)

plot_precision_recall_vs_threshold(precisions, recalls, thresholds)
plt.show()
