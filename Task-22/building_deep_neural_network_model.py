# Task 22

import tensorflow as tf
from tensorflow import keras

# Input layer
input = keras.layers.Input(shape=X_train.shape[1:])

# Hidden layers
hidden1 = keras.layers.Dense(30, activation="relu")(input)
hidden2 = keras.layers.Dense(30, activation="relu")(hidden1)

# Concatenate input and the output of the second hidden layer
concat = keras.layers.Concatenate()([input, hidden2])

# Output layer
output = keras.layers.Dense(1)(concat)

# Model
model = keras.models.Model(inputs=[input], outputs=[output])

# Compile the model
model.compile(loss="mse", optimizer="sgd")
