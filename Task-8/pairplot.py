# Task 08

# Program 11: Pair Plot for Pairwise Relationships

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load penguins dataset
penguins = sns.load_dataset("penguins")

# Create a pair plot to show pairwise relationships
sns.pairplot(data=penguins, hue="species")
