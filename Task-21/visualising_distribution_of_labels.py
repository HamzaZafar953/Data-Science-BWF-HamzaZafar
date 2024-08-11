# Task 21

import numpy as np
import matplotlib.pyplot as plt

def plot_labels_distribution(data_labels):
    counts = np.bincount(data_labels)

    plt.style.use('seaborn-dark-palette')

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(range(10), counts, width=0.8, align='center')
    ax.set(xticks=range(10), xlim=[-1, 10], title='Training data distribution')

    plt.show()

# Plot the distribution of labels in the training data

plot_labels_distribution(train_labels)
