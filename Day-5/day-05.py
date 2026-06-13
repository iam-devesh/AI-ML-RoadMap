"""
### 1. Vectorized Math
Vectorized math: add, subtract, multiply, divide whole arrays element-wise — arr * 2, arr1 + arr2. No loops needed.

Doing math on entire arrays at once without having to write `for` loops in Python. Operations are performed "element-wise" (item by item). This is what makes NumPy so fast.
"""

import numpy as np

print("--- 1. Vectorized Math ---")
arr = np.array([1, 2, 3, 4])
print("arr * 2:", arr * 2) # Output: [2 4 6 8]

arr2 = np.array([10, 20, 30, 40])
print("arr + arr2:", arr + arr2) # Output: [11 22 33 44]
print()

"""
### 2. Universal Functions (ufuncs)
Universal functions: np.sqrt(), np.exp(), np.log(), np.sin() applied to entire arrays at once.

Fast, built-in mathematical functions provided by NumPy that operate on every single element in an array simultaneously.
"""

print("--- 2. Universal Functions (ufuncs) ---")
arr = np.array([1, 4, 9, 16])
print("np.sqrt(arr):", np.sqrt(arr)) # Output: [1. 2. 3. 4.]
print()

"""
### 3. Aggregations & The `axis` Argument
Aggregations: .sum(), .mean(), .min(), .max(), .std() — and the crucial axis argument (axis=0 = down columns, axis=1 = across rows).

Operations that summarize or "aggregate" your data. The `axis` argument is crucial when working with 2D arrays (matrices):
*   `axis=0`: Performs the operation vertically (down the columns).
*   `axis=1`: Performs the operation horizontally (across the rows).
"""

print("--- 3. Aggregations & The axis Argument ---")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])

print("matrix.sum():", matrix.sum())        # Output: 21 (total sum)
print("matrix.sum(axis=0):", matrix.sum(axis=0))  # Output: [5 7 9] (down columns)
print("matrix.sum(axis=1):", matrix.sum(axis=1))  # Output: [ 6 15] (across rows)
print()

"""
### 4. Broadcasting
Broadcasting: how NumPy handles math between arrays of different shapes (e.g., adding a 1D array to each row of a 2D array). Learn the basic rule: dimensions must match or be 1.

A powerful set of rules that allows NumPy to do math between arrays that aren't the exact same shape. NumPy "broadcasts" (stretches) the smaller array so that their shapes match.
"""

print("--- 4. Broadcasting ---")
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]]) # Shape is (2, 3)

row_to_add = np.array([10, 20, 30]) # Shape is (3,)

# NumPy automatically "stretches" row_to_add to add it to both rows!
print("matrix + row_to_add:\n", matrix + row_to_add)
# Output: 
# [[11 22 33]
#  [14 25 36]]
print()

"""
### 5. Comparison Operations
Comparison operations: arr > 5 returns a boolean array (links back to yesterday's boolean indexing).

Checking conditions across an entire array. Returns a new array of the same shape filled with `True` or `False` (booleans). Often used for "boolean indexing" to filter data.
"""

print("--- 5. Comparison Operations ---")
arr = np.array([10, 2, 15, 8, 20])

# Check which elements are greater than 10
print("arr > 10:", arr > 10)
# Output: [False False  True False  True]

# We can use that boolean array to filter the original array
mask = arr > 10
print("arr[mask]:", arr[mask])
# Output: [15 20]
print()