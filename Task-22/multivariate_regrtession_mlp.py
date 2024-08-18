# Task 22

import tensorflow as tf
from tensorflow import keras

# Define the model for multivariate regression
model = keras.models.Sequential([
    keras.layers.Dense(64, activation="relu", input_shape=[8]),  # Adjust input shape based on your data
    keras.layers.Dense(64, activation="relu"),
    keras.layers.Dense(4)  # Four outputs for predicting 4 different values
])

# Compile the model
model.compile(loss="huber", optimizer="adam")

# Summary of the model
model.summary()
