import pandas as pd
import seaborn as sns
# code it yourself (about 2 hours) — type everything:
# Create a Series from a list of 5 numbers; give it a custom index (e.g., ["a","b","c","d","e"]). Access elements by label and by position.
list1=pd.Series([1,2,3,4,5],index=(['a','b','c','d','e']))
print(list1["b"])
# Build a DataFrame from scratch describing 5 people (name, age, city, salary).
df=pd.DataFrame({"name":["abi","abhay","baba","abc","abcd"],"age":[23,34,56,78,89],"city":["Delhi","Mumbai","Kolkata","Chennai","Hyderabad"],"salary":[100000,200000,300000,400000,500000]})
# Run .head(), .info(), .describe(), .shape, .dtypes on it — read what each tells you.
print(df.head())
print(df.info())
print(df.describe())
print(df.shape)
print(df.dtypes)
# Download a real dataset (Titanic from Kaggle, or use seaborn's built-in: sns.load_dataset("titanic")).
titanic_df = sns.load_dataset("titanic")
# Load it and run the full "first look" routine: .head(), .shape, .info(), .describe().
print(titanic_df)
print(titanic_df.head())
print(titanic_df.info())
print(titanic_df.describe())
print(titanic_df.shape)
print(titanic_df.dtypes)
# Access a single column (df["age"]) and confirm it's a Series. Access multiple columns (df[["age","fare"]]) and confirm it's a DataFrame.
print(titanic_df[["age","fare"]])
# Mini-challenge: from the Titanic data, answer in code — how many rows? how many columns? what's the average age? which columns have missing values? (.isna().sum())
print(len(titanic_df))
print(len(titanic_df.columns))
print(titanic_df["age"].mean())
print(titanic_df.isna().sum())
