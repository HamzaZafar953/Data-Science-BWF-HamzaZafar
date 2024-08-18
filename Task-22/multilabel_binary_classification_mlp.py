# Task 22

import tensorflow as tf
from tensorflow import keras

# Define the model for multilabel binary classification
model = keras.models.Sequential([
    keras.layers.Dense(50, activation="relu", input_shape=[8]),  # Adjust input shape based on your data
    keras.layers.Dense(50, activation="relu"),
    keras.layers.Dense(2, activation="sigmoid")  # Two outputs for two binary labels
])

# Compile the model
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

# Summary of the model
model.summary()
