# Task 10 

# Time Series Plotting With Pandas

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate random data for ice-cream sales
start_date = "Jan 1, 2020"
end_date = "Mar 31, 2020"
idx = pd.date_range(start_date, end_date)
items_sold = pd.Series(np.random.randint(25, 50, size=len(idx)), index=idx)

# Additional items for weekly parties
additional_items = pd.Series(10, index=pd.date_range(start_date, end_date, freq="W"))

# Total items including additional items
total_items = items_sold.add(additional_items, fill_value=0)

# Plotting total sales
total_items.plot()
plt.title('Total Items Sold (with additional items)')
plt.xlabel('Date')
plt.ylabel('Items Sold')
plt.show()
