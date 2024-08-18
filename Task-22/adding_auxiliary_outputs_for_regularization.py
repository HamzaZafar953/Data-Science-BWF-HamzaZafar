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

# Main output layer
main_output = keras.layers.Dense(1)(concat)

# Auxiliary output layer
aux_output = keras.layers.Dense(1)(hidden2)

# Model
model = keras.models.Model(inputs=[input_A, input_B], outputs=[main_output, aux_output])

# Compile the model with different loss weights
model.compile(loss=["mse", "mse"], loss_weights=[0.9, 0.1], optimizer="sgd")
