import numpy as np;
# Generate a NumPy array of 100 random exam scores (0–100) using np.random.randint.
exam_score=np.random.randint(0,101,100)
print(exam_score)
# Compute mean, median, std, min, max.

# Count how many scores are above the mean (boolean indexing + .sum()).
# Find the highest and lowest score and their positions (argmax, argmin).
# Normalize the scores to a 0–1 range.
# Wrap the whole thing in a function that takes an array and returns a summary dict.