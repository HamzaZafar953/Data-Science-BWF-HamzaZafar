# Task 08

# Program 16: matplotlib library

# Import the matplotlib library and pyplot module
import matplotlib.pyplot as plt

# Create a simple line plot
def line_plot():
    # Data for plotting
    x = [0, 1, 2, 3, 4, 5]
    y = [0, 1, 4, 9, 16, 25]

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='y = x^2')
    
    # Add titles and labels
    plt.title('Line Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Add legend
    plt.legend()
    
    # Show grid
    plt.grid(True)
    
    # Show the plot
    plt.show()

# Create a simple bar chart
def bar_chart():
    # Data for plotting
    categories = ['A', 'B', 'C', 'D', 'E']
    values = [5, 7, 2, 4, 6]

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.bar(categories, values, color='c', alpha=0.7)
    
    # Add titles and labels
    plt.title('Bar Chart')
    plt.xlabel('Categories')
    plt.ylabel('Values')
    
    # Show grid
    plt.grid(axis='y')
    
    # Show the plot
    plt.show()

# Create a simple scatter plot
def scatter_plot():
    # Data for plotting
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    # Plot the data
    plt.figure(figsize=(10, 5))
    plt.scatter(x, y, color='r', marker='x', s=100)
    
    # Add titles and labels
    plt.title('Scatter Plot')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Show grid
    plt.grid(True)
    
    # Show the plot
    plt.show()

# Call the functions to display the plots
line_plot()
bar_chart()
scatter_plot()
