import pandas as pd

# Create a Series
s = pd.Series([1, 2, 3, 4, 5])
print("Series:\n", s)

# Create a DataFrame
data1 = {
    'Name': ['Subesh', 'Smith', 'Rajan', 'Ritesh', 'amir'],
    'Age': [12, 23, 30, 45, 20],
    'City': ['denkmark', 'kathmandu', 'pokhara', 'htd', 'sydne']
}
df = pd.DataFrame(data1)
print('\nDataFrame:\n', df)

# Selecting row by index
first_row = df.iloc[0]
print('\nFirst row:\n', first_row)

# Adding a new column
df['salary'] = [70000, 5000, 30000, 60000, 500]
print('\nDataFrame with salary column:\n', df)

# Filter data: Show where age > 25
filter_data = df[df['Age'] > 25]
print('\nFiltered Data:\n', filter_data)

# View first 3 rows
print('\nFirst 3 rows:\n', df.head(3))

# Last 3 rows
print('\nLast 3 rows:\n', df.tail(3))

# DataFrame attributes
print('\nDataFrame Index:\n', df.index)
print('\nDataFrame Columns:\n', df.columns)
print('\nDataFrame Data Types:\n', df.dtypes)
print('\nDataFrame Shape:\n', df.shape)
print('\nDataFrame Size:\n', df.size)
print('\nDataFrame Values:\n', df.values)
print('\nDataFrame Transpose:\n', df.T)
print('\nDataFrame Info:')
print(df.info())

# Series with custom index and name
ser = pd.Series([1, 2, 3], index=['a', 'b', 'c'], name="Example Series")

# Handling missing data
data = {
    "Name": ["susasan", "abin", "rajan", "manita", "amrita"],
    "Age": [25, 32, 32, 12, 4],
    "City": ["Bus-park", None, 'Ksheraprur', "parsa", 'parbatipur']
}
df = pd.DataFrame(data)
print("\nIs Null:\n", df.isnull())
df_dropped_rows = df.dropna()
print("\nDataFrame with dropped rows:\n", df_dropped_rows)
df_dropped_columns = df.dropna(axis=1)
print("\nDataFrame with dropped columns:\n", df_dropped_columns)
df_filled_ffill = df.fillna(method="ffill")
print("\nDataFrame with forward fill:\n", df_filled_ffill)
df_filled_bfill = df.fillna(method="bfill")
print("\nDataFrame with backward fill:\n", df_filled_bfill)

# Selecting rows where city is "parsa"
city = df[df["City"] == "parsa"]
print("\nRows where city is 'parsa':\n", city)

# Save DataFrame to CSV and re-load for more operations
data = {
    "Name": ["susasan", "abin", "rajan", "manita", "amrita"],
    "Age": [25, 32, 32, 12, 4],
    "City": ["Bus-park", 'gaidakot', 'Ksheraprur', "parsa", 'parbatipur']
}
df = pd.DataFrame(data)
df.to_csv('example.csv', index=False)
print("\nDataFrame saved successfully!")

# Read the CSV file
df = pd.read_csv('example.csv')
# Show basic info
print("\nDataFrame Info:")
print(df.info())
# Show mean of Age
age_mean = df["Age"].mean()
print("Mean of Age:", age_mean)

# Filter DataFrame for Age > 25 and save as CSV
filter = df[df['Age'] > 25]
print("\nAge > 25:\n", filter)
filter.to_csv('filterdata.csv', index=False)


# Read the filtered data
filtered_df = pd.read_csv('filterdata.csv')
print("\nFiltered DataFrame Info:")
print(filtered_df.info())
print("\nFiltered DataFrame:\n", filtered_df)# Show mean of Age in filtered data
filtered_age_mean = filtered_df["Age"].mean()
print("Mean of Age in filtered data:", filtered_age_mean)
# Describe the filtered data
print("\nFiltered DataFrame Description:\n", filtered_df.describe())
# Describe the original data
print("\nOriginal DataFrame Description:\n", df.describe())
# Sort the original DataFrame by Age
sorted_df = df.sort_values(by='Age')    
print("\nSorted DataFrame by Age:\n", sorted_df)
print("\nSorted DataFrame Info:")
print(sorted_df.info())
# Reset index of sorted DataFrame
reset_sorted_df = sorted_df.reset_index(drop=True)
print("\nReset Sorted DataFrame:\n", reset_sorted_df)
print("\nReset Sorted DataFrame Info:")
print(reset_sorted_df.info())
print("\nReset Sorted DataFrame Columns:\n", reset_sorted_df.columns)
# Save the reset sorted DataFrame
reset_sorted_df.to_csv('sorteddata.csv', index=False)
print("\nSorted DataFrame saved successfully!")
# Read the sorted data
sorted_data_df = pd.read_csv('sorteddata.csv')
print("\nSorted DataFrame Info:")
print(sorted_data_df.info())
print("\nSorted DataFrame:\n", sorted_data_df)

# Show mean of Age in sorted data
sorted_age_mean = sorted_data_df["Age"].mean()
print("Mean of Age in sorted data:", sorted_age_mean)   
# Describe the sorted data
print("\nSorted DataFrame Description:\n", sorted_data_df.describe())
# Describe the original data again
print("\nOriginal DataFrame Description:\n", df.describe())
# Sort the original DataFrame by Name
sorted_by_name_df = df.sort_values(by='Name')
print("\nSorted DataFrame by Name:\n", sorted_by_name_df)
print("\nSorted DataFrame by Name Info:")
print(sorted_by_name_df.info())