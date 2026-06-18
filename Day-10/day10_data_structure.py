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
df["is_child"]=df["age"]<18
print(df["is_child"])
# Create a family_size column by adding the sibsp and parch columns (+1 for the person).
df["family_size"]=df["sibsp"]+df["parch"]+1
print(df["family_size"])
# Use .apply() to make a column extracting the title (Mr, Mrs, Miss) from the name — a stretch, but great practice.
df["title"]=df["name"].apply(lambda x: x.split(",")[1].split(".")[0].strip())
print(df["title"])
# Mini-challenge: write a small reusable function that takes a DataFrame and returns a summary of missing values per column as percentages
def missing_values_summary(df):
    return df.isna().sum()
print(missing_values_summary(df))
