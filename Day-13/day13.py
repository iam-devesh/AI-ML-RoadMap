# 1. Why Seaborn?
# Matplotlib is powerful but verbose — you have to manually set up everything.
# Seaborn is built ON TOP of Matplotlib and makes common plots much easier:
# - It works directly with Pandas DataFrames (just pass column names as strings).
# - It handles grouping and coloring automatically (no manual loops).
# - It looks polished by default (better colors, fonts, and styling out of the box).
# Usage: import seaborn as sns

# 2. Distribution Plots — "What does a single variable look like?"
# These help you understand the shape, spread, and outliers of one column.
# - sns.histplot(df["age"]): A histogram (like plt.hist), but smarter — works with DataFrames directly.
# - sns.kdeplot(df["age"]): A smooth curve (Kernel Density Estimate) instead of bars.
#   Think of it as a "smoothed histogram" — great for comparing overlapping distributions.
# - sns.boxplot(x="class", y="age", data=df): Shows five key stats at a glance:
#   the minimum, Q1 (25th percentile), median (50th), Q3 (75th), and maximum.
#   Dots beyond the whiskers are outliers — values that are unusually high or low.

# 3. Relationship Plots — "How do two variables relate to each other?"
# These help you spot correlations and trends between two numeric columns.
# - sns.scatterplot(x="age", y="fare", data=df): Like plt.scatter, but with DataFrame support.
# - sns.regplot(x="age", y="fare", data=df): Same as scatterplot BUT it adds a regression
#   (trend) line automatically. This line shows the general direction of the relationship
#   (e.g., "do older passengers tend to pay more?").

# 4. Categorical Plots — "How does a number differ across categories?"
# These are designed for when one axis is a category (like class, sex, etc.).
# - sns.barplot(x="class", y="survived", data=df): Plots the MEAN of survived for each class,
#   plus a confidence interval (the thin black line on each bar showing uncertainty).
# - sns.countplot(x="class", data=df): Simply counts how many rows fall into each category.
#   Like df["class"].value_counts() but as a visual bar chart.
# - sns.violinplot(x="class", y="age", data=df): Like a boxplot, but shows the full shape
#   of the distribution as a curved "violin". Wider sections mean more data points at that value.

# 5. The hue Parameter — Seaborn's Superpower
# The `hue` parameter lets you split ANY plot by a category using color.
# Example: sns.barplot(x="class", y="survived", hue="sex", data=df)
# This creates grouped bars — one color for female, another for male — within each class.
# It instantly answers complex questions like:
# "Did women in Third class survive more than men in First class?"
# You can add hue to histplot, scatterplot, boxplot, violinplot — almost everything.

# 6. The Correlation Heatmap — A Key Pre-Modeling Step
# sns.heatmap(df.corr(), annot=True) creates a color-coded grid showing how every
# numeric column relates to every other numeric column.
# - Values range from -1 to +1:
#   +1 = perfect positive correlation (as one goes up, the other always goes up)
#    0 = no relationship at all
#   -1 = perfect negative correlation (as one goes up, the other always goes down)
# - annot=True prints the actual numbers inside each cell so you can read exact values.
# - This is a critical step before building ML models — it helps you pick which
#   features (columns) are most likely to predict your target variable.