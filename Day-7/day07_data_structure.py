import numpy as np;
# Generate a NumPy array of 100 random exam scores (0–100) using np.random.randint.
exam_score=np.random.randint(0,101,100)
print(exam_score)
# Compute mean, median, std, min, max.
mean=np.mean(exam_score)
median=np.median(exam_score)
std=np.std(exam_score)
min=np.min(exam_score)
max=np.max(exam_score)
print(mean,median,std,min,max)
# Count how many scores are above the mean (boolean indexing + .sum()).
hash=exam_score>mean
print(hash.sum())
# Find the highest and lowest score and their positions (argmax, argmin).
highest=np.argmax(exam_score)
lowest=np.argmin(exam_score)
print(highest,lowest)
# Normalize the scores to a 0–1 range.
normalized_score=(exam_score-exam_score.min())/(exam_score.max()-exam_score.min())
print(normalized_score)
# Wrap the whole thing in a function that takes an array and returns a summary dict.
def summary_dict(arr):
    return {
        "mean":np.mean(arr),
        "median":np.median(arr),
        "std":np.std(arr),
        "min":np.min(arr),
        "max":np.max(arr),
        "above_mean":(arr>np.mean(arr)).sum(),
        "below_mean":(arr<np.mean(arr)).sum(),
        "equal_mean":(arr==np.mean(arr)).sum(),
        "normalized":(arr-arr.min())/(arr.max()-arr.min()),
        "highest":np.argmax(arr),
        "lowest":np.argmin(arr),
        "shape":arr.shape,
        "dtype":arr.dtype,
        "ndim":arr.ndim,
        "size":arr.size,
        "sum":np.sum(arr)
        
    }
    print(summary_dict(exam_score))