"""
Day 11: Pandas GroupBy, Aggregation, and Frequency
This file explains how to analyze data in groups using the split-apply-combine strategy.
"""

import pandas as pd
import seaborn as sns

# Load a sample dataset to use in examples (commented out)
# df = sns.load_dataset("titanic")

# ==========================================
# 1. The Split-Apply-Combine Mental Model
# ==========================================
# groupby() doesn't do much on its own. It's a three-step process:
# 1. SPLIT: Break the DataFrame into smaller groups based on a column's values (e.g., separate males and females).
# 2. APPLY: Run a calculation on each group independently (e.g., calculate the mean).
# 3. COMBINE: Put the results back together into a new, summarized DataFrame.

# ==========================================
# 2. Basic groupby()
# ==========================================
# Groups the data by one column, and then calculates the mean for ALL other numeric columns.
# Example: What is the average age, fare, etc., for each class?
# class_averages = df.groupby("class").mean(numeric_only=True)

# ==========================================
# 3. Aggregating Specific Columns
# ==========================================
# Usually, you don't want the mean of every column. You can specify the exact column you want to aggregate.
# Example: What is the survival rate for each sex?
# - df.groupby("sex"): Splits the data by sex.
# - ["survived"]: We only care about the "survived" column.
# - .mean(): Calculates the average survival rate (since survived is 0 or 1, mean = percentage).
# survival_by_sex = df.groupby("sex")["survived"].mean()

# ==========================================
# 4. Multiple Aggregations using .agg()
# ==========================================
# What if you want the mean AND the count? Use .agg() and pass a list of functions.
# Example: Give me the average fare, the total number of people, and the max fare per class.
# fare_stats = df.groupby("class")["fare"].agg(["mean", "count", "max"])

# ==========================================
# 5. Grouping by Multiple Columns
# ==========================================
# You can group by more than one category by passing a list to groupby().
# Example: What is the survival rate broken down by BOTH sex and passenger class?
# survival_by_sex_and_class = df.groupby(["sex", "class"])["survived"].mean()

# ==========================================
# 6. value_counts()
# ==========================================
# A shortcut for counting how many times each unique value appears in a single column.
# It automatically sorts from most frequent to least frequent.
# Example: How many people were in each class?
# class_counts = df["class"].value_counts()
# Note: You can also use df["class"].value_counts(normalize=True) to get percentages!

# ==========================================
# 7. sort_values()
# ==========================================
# After grouping or aggregating, you often want to sort the results to find the highest or lowest values easily.
# Example: Sort the survival rates from highest to lowest.
# sorted_survival = survival_by_sex_and_class.sort_values(ascending=False)
