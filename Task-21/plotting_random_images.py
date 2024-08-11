# Task 21

import random
import matplotlib.pyplot as plt

def plot_images(nb_images_to_plot, train_data):

    # Generate a list of random indices from the training data
    
    random_indices = random.sample(range(len(train_data)), nb_images_to_plot)

    # Plot each image using the random indices
    
    for i, idx in enumerate(random_indices):
        plt.subplot(330 + 1 + i)
        plt.imshow(train_data[idx], cmap=plt.get_cmap('gray'))

    plt.show()

# Plot 9 random images from the training data

nb_images_to_plot = 9
plot_images(nb_images_to_plot, train_images)
