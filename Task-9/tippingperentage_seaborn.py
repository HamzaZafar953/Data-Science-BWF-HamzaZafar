# Task 09

# Tipping Perentage with Seaborn 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Example of using Seaborn for plotting tipping percentage by day
tips = pd.read_csv("examples/tips.csv")
tips["tip_pct"] = tips["tip"] / (tips["total_bill"] - tips["tip"])

sns.barplot(x="tip_pct", y="day", data=tips, orient="h")
plt.show()
