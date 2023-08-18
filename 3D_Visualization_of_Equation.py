import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid of x and y values
x_vals = np.linspace(-1, 1, 100)
y_vals = np.linspace(-1, 1, 100)
x_mesh, y_mesh = np.meshgrid(x_vals, y_vals)

# Calculate the z values based on the equation
z_mesh = np.arccos(x_mesh) - (-1 / (1 - x_mesh**2)**0.5)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x_mesh, y_mesh, z_mesh, cmap='viridis')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of Equation')

plt.show()
