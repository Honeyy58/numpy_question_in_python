import numpy as np


# Q1. Array Addition
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([10, 20, 30, 40])
print(arr1 + arr2)


# Q2. Array Multiplication
arr1 = np.array([2, 4, 6])
arr2 = np.array([3, 5, 7])
print(arr1 * arr2)

# Q3. Add a Scalar to an Array
arr = np.array([10, 20, 30, 40])
print(arr + 5)

# Q4. Multiply Array by a Scalar
arr = np.array([1, 2, 3, 4])
print(arr * 3)

# Q5. Matrix Broadcasting
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr + 10)

# Q6. Find Sum of Array
arr = np.array([5, 10, 15, 20])
print(np.sum(arr))

# Q7. Find Mean of Array
arr = np.array([10, 20, 30, 40, 50])
print(np.mean(arr))

# Q8. Find Maximum and Minimum Value
arr = np.array([12, 45, 7, 89, 23])
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Q9. Row-wise Sum using Axis
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.sum(arr, axis=1))

# Q10. Column-wise Sum using Axis
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(np.sum(arr, axis=0))