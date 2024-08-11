# Task 16

import matplotlib.pyplot as plt
import numpy as np

# Define a function to plot the decision boundary
 
def plot_decision_boundary(model, ax=None):
    if ax is None:
        ax = plt.gca()
        
    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    
    # Create grid to evaluate model
    
    x = np.linspace(xlim[0], xlim[1], 30)
    y = np.linspace(ylim[0], ylim[1], 30)
    Y, X = np.meshgrid(y, x)

    # Shape data
    
    xy = np.vstack([X.ravel(), Y.ravel()]).T
    
    # Get the decision boundary based on the model
    
    P = model.decision_function(xy).reshape(X.shape)
    
    # Plot decision boundary
    
    ax.contour(X, Y, P, levels=[0], alpha=0.5, linestyles=['-'])

# Plot the data and decision boundary

plt.scatter(circle_X[:, 0], circle_X[:, 1], c=circle_y, s=50)
plot_decision_boundary(nonlinear_clf)
plt.scatter(nonlinear_clf.support_vectors_[:, 0], nonlinear_clf.support_vectors_[:, 1], s=50, lw=1, facecolors='none')
plt.show()
