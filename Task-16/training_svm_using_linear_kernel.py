# Task 16

from sklearn import svm

# Define the SVM model with a linear kernel

clf = svm.SVC(kernel='linear', C=1.0)

# Train the SVM model

clf.fit(training_X, training_y)

# Print the model coefficients

print("Model Coefficients:", clf.coef_)
print("Model Intercept:", clf.intercept_)
