# Task 08

# Program 3: Line Plot to Visualize Statistical Estimation

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load fmri dataset
fmri = sns.load_dataset("fmri")

# Create a line plot to visualize statistical estimation
sns.relplot(
    data=fmri, kind="line",
    x="timepoint", y="signal", col="region",
    hue="event", style="event",
)
