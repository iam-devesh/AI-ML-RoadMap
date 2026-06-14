import numpy as np
# Create an array 1–10 and, in one line each: double it, square it, take its square root.
array1=np.arange(1,11)
print(array1*2)
print(array1**2)
print(np.sqrt(array1))
# Create a 3×4 array. Get the sum of each column (axis=0) and each row (axis=1). Make sure you understand which is which.
array2=np.arange(1,13)
array2=array2.reshape((3,4))
print(array2)
print(array2.sum(axis=0))
print(array2.sum(axis=1))
# Normalize an array: subtract its mean and divide by its standard deviation ((arr - arr.mean()) / arr.std()). This is a real ML preprocessing step you'll use constantly.
array3=np.arange(1,13)
array3=(array3-array3.mean())/array3.std()
print(array3)
# Broadcasting practice: create a 3×3 array and add [10, 20, 30] to every row. Observe how it "stretches."
array4=np.arange(1,10).reshape((3,3))
print(array4+[10,20,30])
# Convert an array of Celsius temps to Fahrenheit using vectorized math (C * 9/5 + 32).
array5=np.arange(1,6)
print((array5*9/5)+32)
# Mini-challenge: create a 5×5 array of random numbers, then replace every value below the mean with 0 using boolean indexing + assignment.
array6=np.random.rand(5,5)
print(array6[array6<array6.mean()])

