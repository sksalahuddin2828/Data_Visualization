import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Interactive User Input
a = float(input("Enter the value of 'a': "))
b = float(input("Enter the value of 'b': "))

# Calculations with Pythagorean Theorem
c = np.sqrt(a**2 + b**2)

# Create 3D Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate Points for Visualization
x = np.linspace(0, a, 10)
y = np.linspace(0, b, 10)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)

# Plot the 3D Surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add Labels and Title
ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')
ax.set_title('Pythagorean Theorem Visualization')

# Show the Plot
plt.show()

