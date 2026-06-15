import numpy as np

# Q1. Create a NumPy Array
arr = np.array([10, 20, 30, 40, 50])
print(arr)

# Q2. Create a 3×3 Matrix
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(matrix)

# Q3. Create an Array of Zeros
zeros_arr = np.zeros(5)
print(zeros_arr)

# Q4. Create a 2×4 Zero Matrix
zero_matrix = np.zeros((2, 4))
print(zero_matrix)

# Q5. Create an Array of Ones
ones_arr = np.ones(6)
print(ones_arr)

# Q6. Create a Matrix Using full()
full_matrix = np.full((3, 3), 9)
print(full_matrix)

# Q7. Create Numbers Using arange()
even_numbers = np.arange(0, 20, 2)
print(even_numbers)

# Q8. Create Values Using linspace()
values = np.linspace(0, 1, 6)
print(values)

# Q9. Create an Identity Matrix
identity_matrix = np.eye(5)
print(identity_matrix)

# Q10. Create a Random Integer Matrix
random_matrix = np.random.randint(1, 21, (3, 3))
print(random_matrix)