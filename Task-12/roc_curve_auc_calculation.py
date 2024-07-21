# Task 12

import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score

# Calculate FPR and TPR for various thresholds
fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)

# Plot ROC curve
def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')  # Dashed diagonal
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.grid(True)

plot_roc_curve(fpr, tpr)
plt.show()

# Calculate ROC AUC score
roc_auc = roc_auc_score(y_train_5, y_scores)
print(f"ROC AUC score: {roc_auc}")
