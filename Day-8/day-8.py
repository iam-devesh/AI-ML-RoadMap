# ==========================================
# PANDAS FOUNDATIONS
# ==========================================

# 1. Series
# A 1D labeled array — like a single column with an index. 
# Unlike a regular Python list, a Series has an explicit Index (custom labels for each row).
# Create from a list or dict: pd.Series([10, 20, 30]).

# 2. DataFrame
# A 2D table — rows and labeled columns. The workhorse of Pandas. 
# Think of it as an Excel spreadsheet or a SQL table. It's essentially a collection of Series sharing an index.
# Create from a dict of lists:
# df = pd.DataFrame({"name": ["Alex", "Sam"], "age": [25, 30]})

# 3. Reading Data
# Reading a CSV: pd.read_csv("file.csv") 
# A CSV is a plain-text file storing tabular data. This method is how you'll load almost every dataset into a DataFrame.

# 4. First-look methods (Exploratory Data Analysis)
# These are the first things you run on any new dataset to understand it:
# .head()     - Shows the first 5 rows of the dataset.
# .tail()     - Shows the last 5 rows of the dataset.
# .shape      - Tells you the dimensions (rows, columns).
# .info()     - Summary of DataFrame, including column names, non-null counts, and data types.
# .describe() - Generates basic statistics (mean, std, min, max) for numerical columns.
# .columns    - Returns a list of all column names.
# .dtypes     - Tells you the data type of each column.

# 5. How Pandas relates to NumPy
# Pandas is built on top of NumPy. 
# A DataFrame is essentially labeled NumPy arrays under the hood. Pandas adds row/column labels,
# missing data handling (NaN), and powerful tools for grouping/merging which raw NumPy lacks.