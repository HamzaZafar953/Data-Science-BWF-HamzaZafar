# Task 14

import numpy as np

def cross_entropy(y_true, y_pred):
    m = y_true.shape[0]
    log_likelihood = -np.log(y_pred[range(m), y_true])
    loss = np.sum(log_likelihood) / m
    return loss

# Example usage
y_true = np.array([0, 1, 2])
y_pred = np.array([[0.7, 0.2, 0.1],
                   [0.1, 0.5, 0.4],
                   [0.2, 0.3, 0.5]])

loss = cross_entropy(y_true, y_pred)
print("Cross Entropy Loss:", loss)
