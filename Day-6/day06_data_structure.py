import numpy as np
# Create an array 1–20. Return only the even numbers (boolean indexing).
even=np.arange(1,21)
print(even[even%2==0])
# Given an array, replace all negative values with 0 (np.where or boolean assignment).
array1=np.arange(-10,10,2)
array1=np.where(array1<0,0,array1)
print(array1)
# Find the index of the maximum value in an array (np.argmax).
print(np.argmax(array1))
# Create a 5×5 array counting 1–25 (arange + reshape). Extract the middle 3×3 block with slicing.
array2=np.arange(1,26).reshape((5,5))
print(array2)
# Compute the row-wise and column-wise means of a 2D array.
print(array2.mean(axis=0))
print(array2.mean(axis=1))
# Given two arrays of equal length, count how many positions have equal values (no loop — use comparison + .sum()).
array3=np.array([1,2,3,4,5])
array4=np.array([1,2,3,4,5])
print((array3==array4).sum())
# Normalize a random array to range 0–1 ((arr - arr.min()) / (arr.max() - arr.min())).
array5=np.random.rand(5,5)
print((array5-array5.min())/(array5.max()-array5.min()))
# Stretch challenge: create a 10×10 multiplication table using broadcasting (hint: reshape one array to a column and multiply by a row).
arrow=np.arange(1,11)
column=np.arange(1,11).reshape((10,1))
print(arrow*column)
