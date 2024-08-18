# Task 23

import tensorflow as tf

# Apply convolution using the filters on the images
outputs = tf.nn.conv2d(images, filters, strides=1, padding="SAME")

print("Outputs shape:", outputs.shape)
