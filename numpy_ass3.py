import numpy as np

# Q1. Fancy Indexing (1D Array)
arr1 = np.array([10, 20, 30, 40, 50, 60])
print(arr1[[0, 2, 5]])

# Q2. Fancy Indexing (1D Array)
arr2 = np.array([5, 15, 25, 35, 45])
print(arr2[[1, 4]])

# Q3. Fancy Indexing (2D Array)
arr3 = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]])
print(arr3[[0, 1, 2], [0, 1, 2]])

# Q4. Conditional Selection
arr4 = np.array([5, 12, 18, 25, 30, 7])
print(arr4[arr4 > 15])

# Q5. Conditional Selection
arr5 = np.array([2, 4, 7, 10, 13, 16])
print(arr5[arr5 % 2 == 0])

# Q6. Sorting an Array
arr6 = np.array([25, 10, 40, 5, 30])
print(np.sort(arr6))

# Q7. Find Sorted Indices
arr7 = np.array([50, 20, 70, 10])
print(np.argsort(arr7))

# Q8. Concatenate Arrays
arr8_1 = np.array([1, 2, 3])
arr8_2 = np.array([4, 5, 6])
print(np.concatenate((arr8_1, arr8_2)))

# Q9. Vertical Stacking
arr9_1 = np.array([1, 2, 3])
arr9_2 = np.array([4, 5, 6])
print(np.vstack((arr9_1, arr9_2)))

# Q10. Horizontal Stacking
arr10_1 = np.array([10, 20, 30])
arr10_2 = np.array([40, 50, 60])
print(np.hstack((arr10_1, arr10_2)))