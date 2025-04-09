import numpy as np

# 1. Create a 1D array
a = np.array([1, 2, 3, 4, 5])

# 2. Create a 2D array
b = np.array([[1, 2], [3, 4]])

# 3. Generate a range of numbers
c = np.arange(0, 10, 2)

# 4. Generate evenly spaced numbers
d = np.linspace(0, 1, 5)

# 5. Create an array of zeros
zeros = np.zeros((2, 3))

# 6. Create an array of ones
ones = np.ones((3, 2))

# 7. Create an identity matrix
eye = np.eye(3)

# 8. Generate random floats between 0 and 1
rand_floats = np.random.rand(4)

# 9. Generate random integers
rand_ints = np.random.randint(1, 100, size=(3, 3))

# 10. Get shape of an array
shape = rand_ints.shape

# 11. Reshape an array
reshaped = np.arange(12).reshape(3, 4)

# 12. Flatten a multi-dimensional array
flattened = reshaped.flatten()

# 13. Element-wise addition
sum_array = a + 5

# 14. Element-wise multiplication
prod_array = a * 2

# 15. Matrix multiplication
matrix_prod = np.dot(b, b)

# 16. Calculate mean of an array
mean_val = np.mean(a)

# 17. Calculate standard deviation
std_val = np.std(a)

# 18. Find min and max
min_val = np.min(a)
max_val = np.max(a)

# 19. Conditional selection
greater_than_2 = a[a > 2]

# 20. Replace values using condition
replaced = np.where(a > 3, 99, a)
