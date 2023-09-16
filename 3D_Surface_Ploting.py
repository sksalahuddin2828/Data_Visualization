import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbolic variables
x, y = sp.symbols('x y')

# Define a mathematical expression (e.g., a 3D surface)
expr = sp.sin(sp.sqrt(x**2 + y**2)) / (sp.sqrt(x**2 + y**2))

# Create a meshgrid of x and y values
x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)

# Convert the symbolic expression to a Python function
f = sp.lambdify((x, y), expr, 'numpy')

# Calculate the function values for the meshgrid
Z = f(X, Y)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Surface Plot')

# Show the plot
plt.show()
