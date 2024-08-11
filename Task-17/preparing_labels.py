# Task 17

from keras.utils import to_categorical

# One-hot encoding of labels

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Displaying the first encoded label

print(f'First encoded training label: {train_labels[0]}')
