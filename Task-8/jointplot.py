# Task 08

# Program 10: Joint Plot for Joint and Marginal Distributions

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load penguins dataset
penguins = sns.load_dataset("penguins")

# Create a joint plot to show the joint and marginal distributions
sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")
