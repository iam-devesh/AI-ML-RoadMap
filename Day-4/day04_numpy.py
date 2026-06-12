"""
Day 4: Introduction to NumPy
"""

# pyrefly: ignore [missing-import]
import numpy as np

print("--- 1. Why NumPy ---")
# Arrays are far faster than Python lists for math, and the whole ML stack uses them.
# NumPy arrays are stored in contiguous blocks of memory.
# It allows vectorized operations which avoid slow Python for-loops.

# Example: adding two lists vs adding two arrays
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list_sum = [a + b for a, b in zip(list1, list2)]
print("List sum (Python):", list_sum)

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
arr_sum = arr1 + arr2 # Vectorized addition
print("NumPy Array sum (Vectorized):", arr_sum)


print("\n--- 2. Creating Arrays ---")
# np.array(): Convert a Python list (or tuple) to a NumPy array
arr = np.array([1, 2, 3])
print("np.array([1, 2, 3]):", arr)

# np.zeros(): Create an array filled with zeros
zeros = np.zeros((2, 3)) # 2 rows, 3 columns
print("np.zeros((2, 3)):\n", zeros)

# np.ones(): Create an array filled with ones
ones = np.ones((3, 2)) # 3 rows, 2 columns
print("np.ones((3, 2)):\n", ones)

# np.arange(): Create an array with evenly spaced values within a given interval
# np.arange(start, stop, step)
arange_arr = np.arange(0, 10, 2) 
print("np.arange(0, 10, 2):", arange_arr)

# np.linspace(): Create an array with evenly spaced numbers over a specified interval
# np.linspace(start, stop, num_of_elements)
linspace_arr = np.linspace(0, 1, 5) # 5 elements evenly spaced from 0 to 1
print("np.linspace(0, 1, 5):", linspace_arr)


print("\n--- 3. Array Attributes ---")
example_arr = np.array([[1, 2, 3], [4, 5, 6]])
print("Example Array:\n", example_arr)

# .shape: Tuple of array dimensions (rows, columns)
print("Shape (.shape):", example_arr.shape)

# .dtype: Data-type of the array's elements (e.g., int64, float64)
print("Data type (.dtype):", example_arr.dtype)

# .ndim: Number of array dimensions (axes)
print("Number of dimensions (.ndim):", example_arr.ndim)

# .size: Total number of elements in the array
print("Total size (.size):", example_arr.size)


print("\n--- 4. Indexing & Slicing ---")
# 1D Array (similar to Python lists)
arr_1d = np.array([10, 20, 30, 40, 50])
print("1D Array:", arr_1d)
print("Index 0 (arr_1d[0]):", arr_1d[0])
print("Slice [1:4] (arr_1d[1:4]):", arr_1d[1:4])

# 2D Array
arr_2d = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("\n2D Array:\n", arr_2d)

# arr[row, col] - Accessing a specific element
print("Element at row 1, col 2 (arr_2d[1, 2]):", arr_2d[1, 2])

# arr[:, 0] (whole column) - all rows (:), column 0
print("Whole column 0 (arr_2d[:, 0]):", arr_2d[:, 0])

# arr[1, :] (whole row) - row 1, all columns (:)
print("Whole row 1 (arr_2d[1, :]):", arr_2d[1, :])

# Slicing a sub-matrix (rows 0 to 1, columns 1 to end)
print("Sub-matrix (arr_2d[:2, 1:]):\n", arr_2d[:2, 1:])


print("\n--- 5. Reshaping ---")
# Reshaping allows you to change the shape (rows and columns) without changing the data.
# The total number of elements must remain exactly the same.
original_arr = np.arange(1, 13) # Array with 12 elements (1 to 12)
print("Original 1D array (12 elements):", original_arr)

# Reshape to 3 rows, 4 columns
reshaped_3x4 = original_arr.reshape((3, 4))
print("\nReshaped to 3x4 (.reshape(3, 4)):\n", reshaped_3x4)

# Reshape to 4 rows, 3 columns
reshaped_4x3 = original_arr.reshape((4, 3))
print("\nReshaped to 4x3 (.reshape(4, 3)):\n", reshaped_4x3)

# -1 can be used as a placeholder to let NumPy automatically calculate the dimension
# based on the length of the array and the remaining dimensions.
# Here we specify 2 rows, and NumPy calculates it needs 6 columns (12 / 2 = 6).
reshaped_auto = original_arr.reshape((2, -1))
print("\nReshaped with -1 (.reshape(2, -1)):\n", reshaped_auto)
