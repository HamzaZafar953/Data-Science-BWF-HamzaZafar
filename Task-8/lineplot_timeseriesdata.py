# Task 08

# Program 2: Line Plot to Visualize Time Series Data

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load another example dataset
dots = sns.load_dataset("dots")

# Create a line plot to visualize time series data
sns.relplot(
    data=dots, kind="line",
    x="time", y="firing_rate", col="align",
    hue="choice", size="coherence", style="choice",
    facet_kws=dict(sharex=False),
)
