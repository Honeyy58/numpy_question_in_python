import numpy as np

#01 Array createon and Arrributes
arr = np.array([10,20,30,40,50])

print("Array:",arr)
print("Shape:", arr.shape)
print("Dimensions (ndim):", arr.ndim)
print("Size:", arr.size)
print("data type", arr.dtype)

# Q2. Matrix creation
matrix = np.array([[1,2,3],
                   [4,5,6],
                   [7,8,9,]])
print(matrix)

#3 indexing practice parctice
arr = np.array([10,20,30,40,50])

print(" ",arr[0])
print(" ",arr[2])
print(" ",arr[-2])

# Q4 slicing practice

arr = np.array([5,10,15,20,25,30,35,40])

print("Element from index 2 to 5 ", arr[2:6])

# Q5 Fancy indexing 

arr = np.array([5,10,15,20,25,30])

print(" ", arr[[0,2,4]])

# Q6 brosdcasting
arr = np.array([5,10,15,20,25,30])
print(" ", arr > 15)

# Q7 Broading 
arr = np.array([1,2,3,4,5,6])

print("original array", arr)
print("after Add 10:", arr + 10)

# Q8 Aggreqgates functions
arr = np.array([50,10,30,20,30])

print("sum", np.sum(arr))
print("Mean:",np.mean(arr))
print("Max",np.max(arr))
print("Mini",np.min(arr))

# Q9 storing 
arr = np.array([50,10,40,20,30])

print("oringinal array",arr)
print("sorted Array:", np.sort(arr))

# Q 10 concatenation and stacking 

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

print(np.concatenate((arr1 ,arr2)))
print(np.vstack((arr1, arr2)))