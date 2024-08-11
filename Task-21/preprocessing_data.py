# Task 21

from keras.utils import to_categorical

def preprocess_data(data, label, vector_size, grayscale_size):

    # Normalize to range 0-1
    
    preprocessed_images = data.reshape((data.shape[0], vector_size)).astype('float32') / grayscale_size
    
    # One-hot encode the labels
    
    encoded_labels = to_categorical(label)
    
    return preprocessed_images, encoded_labels

# Preprocessing parameters

vector_size = 28 * 28
grayscale_size = 255

# Preprocessing of the training data

train_images, train_labels = preprocess_data(train_images, train_labels, vector_size, grayscale_size)

# Preprocessing of the testing data

test_images, test_labels = preprocess_data(test_images, test_labels, vector_size, grayscale_size)

# Checking min and max pixel values after normalization

print("Training data")
print(f"- Maximum Value: {train_images.max()}")
print(f"- Minimum Value: {train_images.min()}")

print("\n")

print("Testing data")
print(f"- Maximum Value: {test_images.max()}")
print(f"- Minimum Value: {test_images.min()}")
