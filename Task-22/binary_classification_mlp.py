# Task 22

import tensorflow as tf
from tensorflow import keras

# Define the model for binary classification
model = keras.models.Sequential([
    keras.layers.Dense(20, activation="relu", input_shape=[8]),  # Adjust input shape based on your data
    keras.layers.Dense(20, activation="relu"),
    keras.layers.Dense(1, activation="sigmoid")  # Single output with logistic activation for binary classification
])

# Compile the model
model.compile(loss="binary_crossentropy", optimizer="sgd", metrics=["accuracy"])

# Summary of the model
model.summary()
