"""
Pandas Data Selection, Filtering, and Sorting Concepts
"""

# 1. Selecting columns
# df["col"] -> Returns a Series (one column).
# df[["col1", "col2"]] -> Returns a DataFrame (multiple columns).

# 2. .loc[] — Label-based selection
# df.loc[row_label, "col_name"]
# Works with row labels (index names) and column names.
# Example: df.loc[5, "age"] gets the "age" for the row labeled 5.

# 3. .iloc[] — Position-based selection
# df.iloc[0, 2]
# Works with integer positions like NumPy (0-indexed).
# Example: df.iloc[0, 2] gets the data in the 1st row (index 0), 3rd column (index 2).

# 4. Boolean masks / filtering
# df[df["age"] > 30]
# Keeps only rows meeting a condition. This creates a mask of True/False values.

# 5. Combining conditions
# df[(df["age"] > 30) & (df["sex"] == "female")]
# Use & (AND), | (OR), and you MUST wrap each individual condition in parentheses ().

# 6. Sorting
# df.sort_values("age", ascending=False)

"""
Breakdown of df.sort_values:
- df: The pandas DataFrame.
- .sort_values(...): The method used to sort rows based on values in a column.
- "age": The column name to sort by.
- ascending=False: Sorts in descending order (highest to lowest). Default is True (lowest to highest).

Example:
import pandas as pd
data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 22]}
df = pd.DataFrame(data)

# Sort from oldest to youngest
sorted_df = df.sort_values("age", ascending=False)
"""