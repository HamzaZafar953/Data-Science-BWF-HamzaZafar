# Task 14

import numpy as np

def softmax(z):
    exp_z = np.exp(z)
    return exp_z / np.sum(exp_z, axis=1, keepdims=True)

def cross_entropy_loss(y_true, y_pred):
    m = y_true.shape[0]
    return -np.sum(y_true * np.log(y_pred)) / m

def compute_gradients(X, y_true, y_pred):
    m = X.shape[0]
    return np.dot(X.T, (y_pred - y_true)) / m

def train_softmax_regression(X, y, learning_rate=0.01, n_iterations=1000):
    m, n = X.shape
    K = np.max(y) + 1
    Y_one_hot = np.eye(K)[y]

    Theta = np.random.randn(n, K)
    for iteration in range(n_iterations):
        scores = np.dot(X, Theta)
        probabilities = softmax(scores)
        gradients = compute_gradients(X, Y_one_hot, probabilities)
        Theta -= learning_rate * gradients
        
        if iteration % 100 == 0:
            loss = cross_entropy_loss(Y_one_hot, probabilities)
            print(f"Iteration {iteration}, Loss: {loss}")
            
    return Theta

def predict(X, Theta):
    scores = np.dot(X, Theta)
    probabilities = softmax(scores)
    return np.argmax(probabilities, axis=1)

