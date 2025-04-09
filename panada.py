import pandas as pd
import numpy as np

# 1. Create a DataFrame from dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# 2. View the first few rows
df.head()

# 3. View basic info about the DataFrame
df.info()

# 4. Summary statistics for numeric columns
df.describe()

# 5. Check data types of each column
df.dtypes

# 6. Select a single column
df['Name']

# 7. Select multiple columns
df[['Name', 'Salary']]

# 8. Filter rows based on a condition
df[df['Age'] > 30]

# 9. Add a new column
df['Bonus'] = df['Salary'] * 0.1

# 10. Apply a function to a column
df['Taxed'] = df['Salary'].apply(lambda x: x * 0.8)

# 11. Rename columns
df.rename(columns={'Salary': 'BaseSalary'}, inplace=True)

# 12. Drop a column
df.drop('Taxed', axis=1, inplace=True)

# 13. Sort by a column
df.sort_values(by='Age', ascending=False)

# 14. Reset the index
df.reset_index(drop=True, inplace=True)

# 15. Check for missing values
df.isnull().sum()

# 16. Group by a column (add a group for demo)
df['Department'] = ['HR', 'IT', 'HR', 'IT']
df.groupby('Department')['BaseSalary'].mean()

# 17. Pivot table
df.pivot_table(values='BaseSalary', index='Department', aggfunc='mean')

# 18. Create a Series from a list
s = pd.Series([10, 20, 30, 40])

# 19. Merge two DataFrames
df2 = pd.DataFrame({
    'Name': ['Alice', 'Bob'],
    'City': ['New York', 'Los Angeles']
})
merged = pd.merge(df, df2, on='Name')

# 20. Save DataFrame to CSV (won't write in Jupyter, just syntax)
df.to_csv('output.csv', index=False)
