# Task 17

from keras.datasets import mnist

# Loading the dataset

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Displaying the shapes and lengths of the data

print(f'Training data shape: {train_images.shape}')
print(f'Training labels length: {len(train_labels)}')
print(f'Test data shape: {test_images.shape}')
print(f'Test labels length: {len(test_labels)}')

# Displaying first few training labels

print(f'Training labels: {train_labels[:10]}')
