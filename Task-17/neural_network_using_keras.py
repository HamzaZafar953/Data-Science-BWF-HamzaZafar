# Task 17

from keras import models
from keras import layers

# Building the network

network = models.Sequential()
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
network.add(layers.Dense(10, activation='softmax'))

# Displaying the network summary

network.summary()
