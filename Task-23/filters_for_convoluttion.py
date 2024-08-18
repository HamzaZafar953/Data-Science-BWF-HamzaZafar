# Task 23

import numpy as np

# Create 2 filters: one for vertical lines and one for horizontal lines
filters = np.zeros(shape=(7, 7, channels, 2), dtype=np.float32)
filters[:, 3, :, 0] = 1  # Vertical line
filters[3, :, :, 1] = 1  # Horizontal line

print("Filters shape:", filters.shape)
