# Task 13

# Program 1: Training and Visualizing a Decision Tree

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, export_graphviz

# Load the iris dataset
iris = load_iris()
X = iris.data[:, 2:]  # petal length and width
y = iris.target

# Train a Decision Tree
tree_clf = DecisionTreeClassifier(max_depth=2)
tree_clf.fit(X, y)

# Visualize the trained Decision Tree
export_graphviz(
    tree_clf,
    out_file="iris_tree.dot",
    feature_names=iris.feature_names[2:],
    class_names=iris.target_names,
    rounded=True,
    filled=True
)

