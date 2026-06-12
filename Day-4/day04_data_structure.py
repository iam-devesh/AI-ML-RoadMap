import numpy as np
import time as time
# Create a 1D array of numbers 1–10. Slice the first 5, last 3, every other element.
arr1=np.arange(1,11)
print(arr1[:5])
# Create a 3×3 array using arange + reshape. Print its shape, dtype, and dimensions.
arr2=np.arange(1,10)
arr2=arr2.reshape((3,3))
print(arr2)
print(arr2.shape)
print(arr2.dtype)
print(arr2.ndim)
# From a 2D array, extract a full row, a full column, and a single element.
array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array[1,:])
print(array[:,1])
print(array[1,1])
# Create a 4×4 array of zeros, then set the diagonal to 1 (or just use np.eye() after trying it manually).
# arr4=np.zeros((4,4))
# arr4[np.diag_indices(4)]=1
print(np.eye(4))
# Compare speed: sum a Python list of 1,000,000 numbers vs a NumPy array (use time). See the difference for yourself.
start_time=time.time()
list_sum=sum(range(1000000))
end_time=time.time()
print("List sum:", list_sum)
print("Time taken:", end_time-start_time)

arr_sum=np.sum(np.arange(1000000))
end_time=time.time()
print("Array sum:", arr_sum)
print("Time taken:", end_time-start_time)
# Mini-challenge: create a 5×5 array of random numbers (np.random.rand), then extract all values greater than 0.5 using boolean indexing
arr=np.random.rand(5,5)
print(arr[arr>0.5])