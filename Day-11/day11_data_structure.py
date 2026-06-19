import seaborn as sns
import numpy as np
# Survival rate by sex: df.groupby("sex")["survived"].mean(). Read the result — what does it tell you?
df=sns.load_dataset("titanic")
print(df.groupby("sex")["survived"].mean())
# Survival rate by passenger class. Then by sex and class together.
print(df.groupby("class", observed=False)["survived"].mean())
# Average age and fare per class using .agg(["mean", "median"]).
print(df.groupby("class", observed=False)[["age","fare"]].agg(["mean","median"]))
# Use value_counts() to see how many passengers were in each class, and each embarkation port.
print(df["class"].value_counts())

print(df["embarked"].value_counts())
# ount survivors vs non-survivors within each sex (groupby + .size() or value_counts).
print(df.groupby("sex")["survived"].size())
# Find which group (sex + class combination) had the highest survival rate, sorted.
print(df.groupby(["sex","class"], observed=False)["survived"].mean().sort_values(ascending=False))
# Mini-challenge: build a single summary table showing, per class: passenger count, average age, average fare, and survival rate — all in one .agg() call with a dictionary.
print(df.groupby("class", observed=False).agg({
    "sex":"count",
    "age":"mean",
    "fare":"mean",
    "survived":"mean"
}))
