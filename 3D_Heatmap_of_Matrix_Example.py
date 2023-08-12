import numpy as np
import sympy as sp

# Matrix A
A = np.array([[4, 3], [2, 1]])

# Calculate determinant using numpy
det_A = np.linalg.det(A)
print("Determinant of matrix A:", det_A)

# Calculate determinant using sympy for symbolic expression
A_sym = sp.Matrix(A)
det_A_sym = A_sym.det()
print("Symbolic determinant of matrix A:", det_A_sym)

# Matrix C
C = np.array([[4, 8], [2, 2]])

# Calculate determinant using numpy
det_C = np.linalg.det(C)
print("Determinant of matrix C:", det_C)

# Matrix A
A = np.array([[1, -9, -3], [4, -6, -2], [3, 5, -2]])

# Calculate determinant using numpy
det_A = np.linalg.det(A)
print("Determinant of matrix A:", det_A)

# Matrix B after the row transformation
B = np.array([[1, 1, 1], [2, 3, 4], [0, 1, 2]])

# Calculate determinant using numpy
det_B = np.linalg.det(B)
print("Determinant of matrix B after transformation:", det_B)

import matplotlib.pyplot as plt

# Matrix example
matrix_example = np.array([[4, 3], [2, 1]])

plt.figure(figsize=(6, 4))
plt.imshow(matrix_example, cmap='viridis', interpolation='nearest')
plt.colorbar()
plt.title("Heatmap of Matrix Example")
plt.show()
