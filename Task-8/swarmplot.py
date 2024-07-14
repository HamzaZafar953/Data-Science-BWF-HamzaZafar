# Task 08

# Program 7: Swarm Plot for Categorical Data

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Visualize categorical data using swarm plot
sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")
