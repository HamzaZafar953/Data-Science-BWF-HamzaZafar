# Task 09

# Bar Plots with Pandas

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Example of creating bar plots with Pandas DataFrame
data = pd.Series(np.random.uniform(size=16), index=list("abcdefghijklmno"))
fig, axes = plt.subplots(2, 1)
data.plot.bar(ax=axes[0], color="black", alpha=0.7)
data.plot.barh(ax=axes[1], color="black", alpha=0.7)
plt.show()

# Example of stacked bar plot with DataFrame
df = pd.DataFrame(np.random.uniform(size=(6, 4)),
                  index=["one", "two", "three", "four", "five", "six"],
                  columns=pd.Index(["A", "B", "C", "D"], name="Genus"))
df.plot.barh(stacked=True, alpha=0.5)
plt.show()
