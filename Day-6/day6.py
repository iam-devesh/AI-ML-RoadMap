import numpy as np
# Goal: Cement NumPy by solving problems without writing loops. Forcing vectorized solutions is how arrays go from "I've seen this" to "I can use this."
# 1. Quick warm-up (about 30 min)

# Skim your Day 4–5 notes. Re-run a couple of examples from memory: create an array, reshape it, normalize it, aggregate with axis. Just to reload it all into your head.
array1=np.array([1,2,3,4,5,6,7,8,9,10])
print(array1)
array1=array1.reshape((5,2))
print(array1)
print(array1.sum(axis=0))
print(array1.sum(axis=1))