# Task 22

import tensorflow as tf
from tensorflow import keras

# Define the model for multiclass classification
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=[28, 28]),  # For image data, adjust for other types of data
    keras.layers.Dense(300, activation="relu"),
    keras.layers.Dense(100, activation="relu"),
    keras.layers.Dense(10, activation="softmax")  # Output layer with softmax for multiclass classification
])

# Compile the model
model.compile(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

# Summary of the model
model.summary()
