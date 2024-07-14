# Task 08

# Program 12: Complex Figure Using PairGrid

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load penguins dataset
penguins = sns.load_dataset("penguins")

# Create a complex figure using PairGrid
g = sns.PairGrid(penguins, hue="species", corner=True)
g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
g.map_lower(sns.scatterplot, marker="+")
g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
g.add_legend(frameon=True)
g.legend.set_bbox_to_anchor((.61, .6))
