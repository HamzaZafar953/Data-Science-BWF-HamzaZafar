# Task 21

from keras import models
from keras import layers

hidden_units = 256
nb_unique_labels = 10
vector_size = 784  # Assuming a 28x28 input image

def define_network_architecture():
    network = models.Sequential()
    network.add(layers.Dense(vector_size, activation='relu', input_shape=(vector_size,)))  # Input layer
    network.add(layers.Dense(512, activation='relu'))  # Hidden layer
    network.add(layers.Dense(nb_unique_labels, activation='softmax'))  # Output layer
    return network

# Generate the network architecture

network = define_network_architecture()

# Display the graphical representation of the network

from keras.utils.vis_utils import plot_model
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

plot_model(network, to_file='network_architecture.png', show_shapes=True, show_layer_names=True)
img = mpimg.imread('network_architecture.png')
plt.imshow(img)
plt.axis('off')
plt.show()
