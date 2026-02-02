# # Question1
# #A) 4*4 Identity matrix
# import numpy as np
#
# # Create 4x4 identity matrix
# identity_matrix = np.identity(4)
#
# print("4x4 Identity Matrix:")
# print(identity_matrix)

#B) two 3*3 matrix and add and mul
import numpy as np

# Generate two 3x3 matrices with random integers from 1 to 9
matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

print("Matrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)


addition = matrix1 + matrix2
print("\nMatrix Addition:")
print(addition)


multiplication = np.dot(matrix1, matrix2)
print("\nMatrix Multiplication:")
print(multiplication)

