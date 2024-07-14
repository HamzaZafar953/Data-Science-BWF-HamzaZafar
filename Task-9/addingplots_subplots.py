# Task 09

# Adding plots to subplots

import matplotlib.pyplot as plt
import numpy as np

# Create a new figure and subplots
fig, axes = plt.subplots(2, 3)

# Plot on each subplot
for i in range(2):
    for j in range(3):
        axes[i, j].plot(np.random.standard_normal(50).cumsum(), color='black', linestyle='dashed')

# Display the figure with subplots
plt.show()
