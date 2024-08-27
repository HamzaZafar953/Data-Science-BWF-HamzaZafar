# Task 26

# Display top 5 rows
print(housing.head())

# Display info about the DataFrame
print(housing.info())

# Display value counts for the "ocean_proximity" column
print(housing["ocean_proximity"].value_counts())

# Display summary statistics for numerical attributes
print(housing.describe())
