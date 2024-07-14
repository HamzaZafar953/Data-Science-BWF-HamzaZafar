#Task 08

# Program 15: pandas library

# Import the pandas library
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'Score': [85, 90, 78, 88, 92]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Display basic information about the DataFrame
print("\nBasic Information:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# Sort the DataFrame by 'Score'
sorted_df = df.sort_values(by='Score', ascending=False)
print("\nDataFrame Sorted by Score:")
print(sorted_df)

# Filter the DataFrame for people older than 25
filtered_df = df[df['Age'] > 25]
print("\nPeople Older Than 25:")
print(filtered_df)

# Add a new column 'Pass' based on 'Score'
df['Pass'] = df['Score'] >= 80
print("\nDataFrame with Pass Column:")
print(df)

# Group by 'City' and calculate mean 'Score'
grouped_df = df.groupby('City')['Score'].mean().reset_index()
print("\nMean Score by City:")
print(grouped_df)

# Save the DataFrame to a CSV file
df.to_csv('output.csv', index=False)
print("\nDataFrame saved to output.csv")
