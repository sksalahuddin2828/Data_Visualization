import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, Eq, solve
from ipywidgets import interactive
from IPython.display import display

# Section 1: Introduction and Mathematical Foundations
print("Welcome to the Non-Singular Matrix Exploration Project\n")
print("In this project, we'll dive into the world of non-singular matrices and explore their properties.")

# Sample matrix
A = np.array([[2, 3], [1, 4]])

# Calculate determinant using Numpy
det_A = np.linalg.det(A)
print(f"Determinant of Matrix A: {det_A}\n")

# Section 2: Interactive 2D Determinant Visualization
plt.figure(figsize=(8, 6))
plt.imshow(A, cmap='viridis', interpolation='none')
plt.title(f"2D Matrix Visualization\nDeterminant: {det_A:.2f}")
plt.colorbar()
plt.show()

# Section 3: Interactive 3D Determinant Visualization
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
det_B = np.linalg.det(B)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
X, Y = np.meshgrid(range(B.shape[0]), range(B.shape[1]))
ax.plot_surface(X, Y, B, cmap='viridis')

ax.set_title(f"3D Matrix Visualization\nDeterminant: {det_B:.2f}")
plt.show()

# Section 4: Mathematical Dance and Symbolic Expressions
a, b, c = symbols('a b c')
eq = Eq(a + 2*b - c, 0)
sol = solve(eq, c)

print("Solving equation:", eq)
print("Solution for c:", sol[0])

# Section 5: Real-Life Applications and Challenges
print("\nApplications of Non-Singular Matrices:")
print("Non-singular matrices play a crucial role in various fields such as computer graphics, physics simulations, and cryptography.\n")

# Sample interactive challenge (you can create more)
def interactive_challenge(a, b):
    result = a + 2*b
    print(f"For a = {a} and b = {b}, the result is:", result)

interactive(interactive_challenge, a=(0, 10), b=(0, 10))

# Section 6: Artistic Mathematical Visualizations and Poetry
print("\nMathematical Poetry:")
print("Non-singular matrices dance,\nIn equations, they find their stance.\nDeterminants tell their graceful tale,\nIn matrices' world, they prevail.\n")

# Conclusion
print("\nThank you for joining us in this exploration of non-singular matrices.")
print("We hope you enjoyed the journey and gained insights into their beauty and applications.")
