# Task 14

from sklearn.linear_model import LogisticRegression
from sklearn import datasets

# Load the iris dataset
iris = datasets.load_iris()
X = iris["data"][:, (2, 3)]  # petal length, petal width
y = iris["target"]

# Train Softmax Regression model
softmax_reg = LogisticRegression(multi_class="multinomial", solver="lbfgs", C=10)
softmax_reg.fit(X, y)

# Making predictions
pred_class = softmax_reg.predict([[5, 2]])
pred_prob = softmax_reg.predict_proba([[5, 2]])

print("Predicted class:", pred_class)
print("Predicted probabilities:", pred_prob)
