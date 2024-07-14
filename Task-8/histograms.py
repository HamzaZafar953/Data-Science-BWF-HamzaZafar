# Task 08

# Program 5: Histograms and Kernel Density Estimation

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Visualize distributions using histograms and kernel density estimation
sns.displot(data=tips, x="total_bill", col="time", kde=True)
