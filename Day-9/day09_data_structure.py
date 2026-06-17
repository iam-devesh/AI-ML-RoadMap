import pandas as pd
import seaborn as sns
df=sns.load_dataset("titanic")
# print(df.head(10))
# select just the age column, then select age and fare together. Confirm the types (Series vs DataFrame).
# print(df["age"])
# print(df[["age","fare"]])
# Use .iloc to grab the first 5 rows and first 3 columns.
# print(df.iloc[:5,:3])
# Use .loc to select specific columns by name for the first 10 rows.
print(df.loc[0:10,"age"])
# Filter: all passengers older than 50.
print(df[df["age"]>50])
# Filter with two conditions: female passengers in 1st class (& with parentheses).
print(df[(df["sex"]=="female") & (df["class"]=="First")])
# Filter: passengers who paid a fare above the average fare (combine a calculation with a mask).
mask=df["fare"]>df["fare"].mean()
print("mask. ",df[mask])
# Sort the data by fare, highest first, and show the top 10.
print(df.sort_values("fare",ascending=False).head(10))
# Mini-challenge: what was the survival rate of passengers under 18? (Filter to under-18, then take the mean of the survived column.) Compare it to the overall survival rate.
mask1=df["age"]<18
print(df[mask1]["survived"].mean())