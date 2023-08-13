import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, Matrix, conjugate
from sympy.utilities.lambdify import lambdify

# Example 1: Check if a matrix is Hermitian
A = np.array([[3, 2+1j], [2-1j, 4]])
A_conjugate = np.conjugate(A)
A_transpose = np.transpose(A)
is_hermitian = np.allclose(A_conjugate, A_transpose)

# Example 2: Calculate determinant of Hermitian matrix
x, y, z, w = symbols('x y z w')
A_sym = Matrix([[x, y+1j*z], [y-1j*z, w]])
det_A = A_sym.det()

# Example 1 Visualization
plt.figure(figsize=(8, 6))
plt.imshow(np.real(A), cmap='coolwarm', interpolation='none')
plt.colorbar()
plt.title("Real Part of Hermitian Matrix")
plt.show()

# Example 2 Visualization
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
x_vals = np.linspace(-5, 5, 50)
y_vals = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x_vals, y_vals)

# Create a function from the symbolic expression
det_A_func = lambdify((x, y, z, w), det_A, "numpy")

# Evaluate the function on the meshgrid
Z = det_A_func(X, Y, 1, 4)

ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_title("Determinant of Hermitian Matrix")
plt.show()


