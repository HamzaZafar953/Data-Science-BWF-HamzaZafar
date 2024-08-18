# Task 23

from sklearn.datasets import load_sample_image
import numpy as np

# Load sample images
china = load_sample_image("china.jpg") / 255
flower = load_sample_image("flower.jpg") / 255

# Store the images in a numpy array
images = np.array([china, flower])

# Get the dimensions of the images
batch_size, height, width, channels = images.shape
print("Batch size:", batch_size)
print("Height:", height)
print("Width:", width)
print("Channels:", channels)
