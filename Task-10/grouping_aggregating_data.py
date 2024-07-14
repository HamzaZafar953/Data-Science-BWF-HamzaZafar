# Task 10

# Grouping and Aggregating Data with Pandas

import pandas as pd

# Continuing from the previous DataFrame example
df = pd.DataFrame({'A': range(1, 10), 'B': ["I", "like", "to", "play", "games", "and", "will", "not", "change"]})

# Grouping by the length of column B and calculating mean of column A
grouped_df = df.groupby(df['B'].apply(len)).mean()

# Renaming columns for clarity
grouped_df = grouped_df.rename(columns={'A': 'Mean of A'})

# Displaying the grouped DataFrame
print(grouped_df)

