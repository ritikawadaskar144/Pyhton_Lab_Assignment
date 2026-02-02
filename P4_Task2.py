import numpy as np

print("Enter elements of 5x3 matrix:")
matrix_5x3 = []
for i in range(5):
    row = list(map(int, input(f"Enter 3 elements for row {i+1}: ").split()))
    matrix_5x3.append(row)


print("\nEnter elements of 3x2 matrix:")
matrix_3x2 = []
for i in range(3):
    row = list(map(int, input(f"Enter 2 elements for row {i+1}: ").split()))
    matrix_3x2.append(row)

A = np.array(matrix_5x3)
B = np.array(matrix_3x2)

print("\n5x3 Matrix:")
print(A)

print("\n3x2 Matrix:")
print(B)

product = np.dot(A, B)

print("\nProduct Matrix (5x2):")
print(product)
