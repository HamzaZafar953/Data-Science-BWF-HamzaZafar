# Task 08

# Program 8: Violin Plot for Underlying Distribution

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Visualize the underlying distribution with a violin plot
sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)
