import numpy as np
# Create an array 1–20. Return only the even numbers (boolean indexing).
even=np.arange(1,21)
print(even[even%2==0])
# Given an array, replace all negative values with 0 (np.where or boolean assignment).
# Find the index of the maximum value in an array (np.argmax).
# Create a 5×5 array counting 1–25 (arange + reshape). Extract the middle 3×3 block with slicing.
# Compute the row-wise and column-wise means of a 2D array.
# Given two arrays of equal length, count how many positions have equal values (no loop — use comparison + .sum()).
# Normalize a random array to range 0–1 ((arr - arr.min()) / (arr.max() - arr.min())).
# Stretch challenge: create a 10×10 multiplication table using broadcasting (hint: reshape one array to a column and multiply by a row).
