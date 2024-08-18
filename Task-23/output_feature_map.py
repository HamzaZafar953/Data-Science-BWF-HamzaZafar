# Task 23

import matplotlib.pyplot as plt

# Visualize the second feature map of the first image
plt.imshow(outputs[0, :, :, 1], cmap="gray")
plt.title("Output Feature Map")
plt.show()
