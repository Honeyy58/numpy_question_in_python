import numpy as np

# Q1. Array Attributes
arr = np.array([10, 20, 30, 40, 50])

print("Shape:", arr.shape)
print("Dimensions:", arr.ndim)
print("Size:", arr.size)
print("dtype:", arr.dtype)

# Q2. Find Array Shape
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]])

print(arr2.shape)

# Q3. 1D Indexing
arr3 = np.array([5, 10, 15, 20, 25])

print(arr3[0])
print(arr3[-1])

# Q4. 2D Indexing
arr4 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

print(arr4[1, 1])

# Q5. 2D Indexing
arr5 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print(arr5[2, 2])

# Q6. 1D Slicing
arr6 = np.array([10, 20, 30, 40, 50, 60])

print(arr6[1:5])

# Q7. 1D Slicing
arr7 = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr7[:5])

# Q8. 2D Slicing
arr8 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])

print(arr8[:2])

# Q9. 2D Slicing
arr9 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])

print(arr9[:, :2])

# Q10. Boolean Indexing
arr10 = np.array([5, 12, 18, 25, 30, 7])

print(arr10[arr10 > 15])