# Task 08

# Program 4: Scatter Plot with Linear Regression Model

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Enhance a scatterplot by including a linear regression model
sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")
