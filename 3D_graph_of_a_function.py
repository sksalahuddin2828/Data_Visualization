# 3D graph of a function f(x) = x^2 + 3x

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(x):
    return x**2 + 3*x

x_values = np.array([0, 1])
y_values = f(x_values)

# Generate data for 3D plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = f(X)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the function surface
ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)

# Plot the points (x, f(x)) on the surface
ax.scatter(x_values, y_values, f(x_values), color='red', s=100, label='Points (x, f(x))')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(X)')
ax.set_title('3D Visualization of f(x) = x^2 + 3x')

# Show legend
ax.legend()

# Show the plot
plt.show()
