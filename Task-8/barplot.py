# Task 08

# Program 9: Bar Plot for Mean Value and Confidence Interval

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load an example dataset
tips = sns.load_dataset("tips")

# Show mean value and confidence interval using bar plot
sns.catplot(data=tips, kind="bar", x="day", y="total_bill", hue="smoker")
