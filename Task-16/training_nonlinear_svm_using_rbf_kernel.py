# Task 16

from sklearn import svm

# Define the non-linear SVM model with an RBF kernel

nonlinear_clf = svm.SVC(kernel='rbf', C=1.0)

# Train the non-linear SVM model

nonlinear_clf.fit(circle_X, circle_y)

# Print the number of support vectors

print("Number of support vectors:", len(nonlinear_clf.support_vectors_))
