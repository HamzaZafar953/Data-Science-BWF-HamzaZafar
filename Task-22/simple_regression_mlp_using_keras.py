# Task 22

import tensorflow as tf
from tensorflow import keras

# Define the model for a regression task
model = keras.models.Sequential([
    keras.layers.Dense(30, activation="relu", input_shape=[8]),  # Adjust input shape based on your data
    keras.layers.Dense(30, activation="relu"),
    keras.layers.Dense(1)  # Single output for regression
])

# Compile the model
model.compile(loss="mean_squared_error", optimizer="sgd")

# Summary of the model
model.summary()
