# Task 08

# Program 6: Empirical Cumulative Distribution Function

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Visualize the empirical cumulative distribution function
sns.displot(data=tips, kind="ecdf", x="total_bill", col="time", hue="smoker", rug=True)
