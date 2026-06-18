import pandas as pd
import seaborn as sns
# Run .isna().sum() to see exactly which columns have missing values and how many.
df=sns.load_dataset("titanic")
print(df.isna().sum())
# Fill missing age values with the median age (df["age"].fillna(df["age"].median())).
df["age"]=df["age"].fillna(df["age"].median())
print(df.isna().sum())
# The deck/cabin column is mostly empty — drop it entirely.
df=df.drop("deck",axis=1)
# Drop any remaining rows with missing values and compare .shape before and after.
print(df.shape)
# Create a new column is_child that's True when age < 18 (use a comparison or .apply()).
# Create a family_size column by adding the sibsp and parch columns (+1 for the person).
# Use .apply() to make a column extracting the title (Mr, Mrs, Miss) from the name — a stretch, but great practice.
# Mini-challenge: write a small reusable function that takes a DataFrame and returns a summary of missing values per column as percentages