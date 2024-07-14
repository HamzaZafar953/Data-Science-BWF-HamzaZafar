# Task 10

# Dataframes with Pandas

import pandas as pd

# Creating Series for DataFrame
a = pd.Series(range(1, 10))
b = pd.Series(["I", "like", "to", "play", "games", "and", "will", "not", "change"], index=range(0, 9))

# Creating a DataFrame
df = pd.DataFrame({'A': a, 'B': b})

# Displaying the DataFrame
print(df)
