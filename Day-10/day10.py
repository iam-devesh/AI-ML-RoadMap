"""
Day 10: Pandas Data Cleaning and Manipulation
This file explains core data cleaning operations in Pandas, with examples.
"""

import pandas as pd
import numpy as np

# ==========================================
# 1. Finding missing data
# ==========================================
# Missing data in Pandas is usually represented as NaN (Not a Number) or None.
# - .isna(): Returns a DataFrame of booleans (True if missing, False if not).
# - .isna().sum(): Counts the total number of missing values per column.
# - .isna().mean(): Returns the proportion/percentage of missing values per column.
# Example usage (commented out):
# df.isna().sum()
# df.isna().mean()

# ==========================================
# 2. Dropping missing data (.dropna())
# ==========================================
# If rows or columns have missing data, you can drop them.
# - axis: axis=0 drops rows (default), axis=1 drops columns.
# - how: how='any' drops if at least one value is missing (default), how='all' drops only if ALL values are missing.
# - thresh: e.g., thresh=5 keeps a row ONLY if it has at least 5 non-missing values.
# Example:
# df.dropna(axis=0, how='any')

# ==========================================
# 3. Filling missing data (.fillna())
# ==========================================
# Instead of dropping, you can replace NaN with a specific value.
# - Constant: df["age"].fillna(0)
# - Mean/Median: df["age"].fillna(df["age"].mean())
# - Forward fill: df.fillna(method="ffill") propagates the last valid observation forward (useful for time-series).

# ==========================================
# 4. When to drop vs fill?
# ==========================================
# - Drop: When missingness is very small (e.g., 5 missing rows in 100k) or the column is mostly empty (e.g., 80% missing).
# - Fill: When the column is valuable and you can reasonably estimate it (like using the mean age), keeping the rest of the row's data intact.

# ==========================================
# 5. Adding/transforming columns
# ==========================================
# You can create new columns based on existing ones using simple vectorized math.
# Example:
# df["age_in_months"] = df["age"] * 12

# ==========================================
# 6. Using .apply()
# ==========================================
# Runs a specific Python function across every element in a column.
# Example:
# df["name_length"] = df["name"].apply(len)

# ==========================================
# 7. Dropping columns
# ==========================================
# Used to remove irrelevant columns from your DataFrame.
# Example (must specify axis=1 to indicate columns):
# df = df.drop("column_name", axis=1)

# ==========================================
# 8. Replacing values & Fixing Data Types
# ==========================================
# - .replace(): Swaps specific values. 
#   Example: df["gender"] = df["gender"].replace({"M": 0, "F": 1})
# - .astype(): Forces a column into a specific data type (e.g., converting strings to integers).
#   Example: df["price"] = df["price"].astype(int)