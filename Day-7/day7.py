"""
Day 7 Review: Core Python & NumPy Concepts
This file contains explanations and brief code examples for all the topics in your review checklist.
"""

import numpy as np

# ==========================================
# 1. Lists, tuples, dicts, sets — and when to use each
# ==========================================
"""
- List: Ordered, mutable (changeable). Use when order matters and you need to add/remove items.
- Tuple: Ordered, immutable (unchangeable). Use for fixed collections of data that shouldn't change.
- Dict: Key-value pairs. Use for fast lookups by a name or ID instead of an index.
- Set: Unordered, unique elements. Use to remove duplicates or for fast membership testing (e.g., "is x in set?").
"""
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_dict = {"name": "Alice", "age": 25}
my_set = {1, 2, 2, 3} # Becomes {1, 2, 3} automatically


# ==========================================
# 2. Loops, conditionals, functions that return values
# ==========================================
"""
- Loops: Iterate over sequences (lists, arrays, etc.) to repeat actions.
- Conditionals: Execute code conditionally based on True/False logic (if/elif/else).
- Functions: Reusable blocks of code that take inputs, do work, and `return` results.
"""
def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Example loop using the function
for i in range(1, 4):
    is_even = check_even(i)


# ==========================================
# 3. List/dict comprehensions
# ==========================================
"""
A concise, fast "one-liner" way to create lists or dictionaries based on existing iterables.
"""
# Instead of a for loop, we do it in one line:
squares_list = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]
squares_dict = {x: x**2 for x in range(3)} # {0: 0, 1: 1, 2: 4}


# ==========================================
# 4. try/except error handling
# ==========================================
"""
Used to catch exceptions so your program doesn't crash if something goes wrong (e.g., dividing by zero).
"""
try:
    result = 10 / 0
except ZeroDivisionError:
    result = 0 # Program handles the error safely instead of crashing


# ==========================================
# 5. NumPy: creating arrays, .shape, .dtype
# ==========================================
"""
- np.array(): Converts a list to a NumPy array.
- .shape: Returns a tuple showing the dimensions (rows, columns).
- .dtype: Shows the data type of the array's elements (e.g., int64, float64).
"""
arr = np.array([[1, 2, 3], [4, 5, 6]])
# arr.shape -> (2, 3)  (2 rows, 3 columns)
# arr.dtype -> int64


# ==========================================
# 6. Indexing & slicing (1D and 2D)
# ==========================================
"""
Extracting specific elements or subarrays. 
For 2D, the format is array[row_slice, column_slice]
"""
arr_1d = np.array([10, 20, 30, 40])
slice_1d = arr_1d[1:3] # [20, 30]

arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
element = arr_2d[0, 1]     # Row 0, Col 1 -> 2
slice_2d = arr_2d[:, 1:]   # All rows, cols from index 1 to end
# [[2, 3],
#  [5, 6],
#  [8, 9]]


# ==========================================
# 7. Reshaping
# ==========================================
"""
Changing the shape (dimensions) of an array without changing its data.
The total number of elements must remain exactly the same.
"""
arr = np.arange(1, 7) # [1, 2, 3, 4, 5, 6] (6 elements)
reshaped = arr.reshape(2, 3) 
# [[1, 2, 3],
#  [4, 5, 6]]


# ==========================================
# 8. Vectorized math & universal functions
# ==========================================
"""
- Vectorized math: Operations apply element-wise without explicit loops, making them incredibly fast.
- ufuncs: NumPy's built-in functions that operate on whole arrays (like np.sqrt, np.exp).
"""
arr = np.array([1, 4, 9])
math_result = arr * 2    # [2, 8, 18]
ufunc_result = np.sqrt(arr) # [1., 2., 3.]


# ==========================================
# 9. Aggregations with axis=0 vs axis=1
# ==========================================
"""
Summarizing data (sum, mean, max, min, std).
- axis=0: Squashes the rows together (calculates vertically down the columns).
- axis=1: Squashes the columns together (calculates horizontally across the rows).
"""
matrix = np.array([[1, 2], 
                   [3, 4]])
# matrix.sum(axis=0) -> [4, 6]
# matrix.sum(axis=1) -> [3, 7]


# ==========================================
# 10. Broadcasting
# ==========================================
"""
How NumPy handles math between arrays of different shapes. The smaller array is "stretched" to match the larger one so element-wise operations can happen.
"""
matrix = np.array([[1, 2], [3, 4]]) # Shape (2, 2)
row = np.array([10, 20])            # Shape (2,)

# 'row' gets added to both rows of 'matrix'
broadcast_result = matrix + row 
# [[11, 22], 
#  [13, 24]]


# ==========================================
# 11. Boolean indexing
# ==========================================
"""
Filtering arrays using a boolean mask (an array of True/False). You provide a condition, get a mask of booleans, and use it to extract only the True values.
"""
arr = np.array([10, 15, 20, 25])
mask = arr > 15   # [False, False, True, True]
filtered_arr = arr[mask] # [20, 25]

# Spend time only on your yellows and reds. Don't re-drill what's already solid — that's comfort, not progress.
# For each weak spot: re-read your notes, find one example, and write a fresh small script from scratch (no copying).
# If everything's green, do a few mixed problems from Day 6 again from memory to confirm.