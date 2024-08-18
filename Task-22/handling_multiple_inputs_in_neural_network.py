# Task 22

import tensorflow as tf
from tensorflow import keras

# Input layers
input_A = keras.layers.Input(shape=[5])
input_B = keras.layers.Input(shape=[6])

# Hidden layers
hidden1 = keras.layers.Dense(30, activation="relu")(input_B)
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)

# Concatenate inputs
concat = keras.layers.concatenate([input_A, hidden2])

# Output layer
output = keras.layers.Dense(1)(concat)

# Model
model = keras.models.Model(inputs=[input_A, input_B], outputs=[output])

# Compile the model
model.compile(loss="mse", optimizer="sgd")
