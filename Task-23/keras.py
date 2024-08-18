# Task 23

from tensorflow import keras

# Create a Conv2D layer using Keras with 32 filters of size 3x3, SAME padding, and ReLU activation
conv_layer = keras.layers.Conv2D(filters=32, kernel_size=3, strides=1, padding="SAME", activation="relu")

print("Convolutional Layer created with 32 filters, 3x3 kernel size, and ReLU activation.")


# Create a MaxPooling2D layer using Keras with pool size 2x2
max_pool = keras.layers.MaxPool2D(pool_size=2)

print("MaxPooling2D Layer created with pool size 2x2.")
