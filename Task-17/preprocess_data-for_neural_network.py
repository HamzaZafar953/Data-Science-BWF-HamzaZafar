# Task 17

# Reshaping and scaling the training and test images

train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255

test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255

# Displaying a sample image before and after preprocessing

import matplotlib.pyplot as plt

digit = train_images[4].reshape(28, 28)
plt.imshow(digit, cmap=plt.cm.binary)
plt.show()
