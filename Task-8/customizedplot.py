# Task 08

# Program 13: Customized Plot with Additional Settings

# Import seaborn
import seaborn as sns

# Apply the default theme
sns.set_theme()

# Load penguins dataset
penguins = sns.load_dataset("penguins")

# Customize a plot with additional seaborn and matplotlib settings
sns.set_theme(style="ticks", font_scale=1.25)
g = sns.relplot(
    data=penguins,
    x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g",
    palette="crest", marker="x", s=100,
)
g.set_axis_labels("Bill length (mm)", "Bill depth (mm)", labelpad=10)
g.legend.set_title("Body mass (g)")
g.figure.set_size_inches(6.5, 4.5)
g.ax.margins(.15)
g.despine(trim=True)
