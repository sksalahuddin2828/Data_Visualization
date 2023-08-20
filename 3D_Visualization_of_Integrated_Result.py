import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a grid of 'a' and 'x' values
a_values = np.linspace(0.1, 2, 50)
x_values = np.linspace(0, 1, 50)
a_grid, x_grid = np.meshgrid(a_values, x_values)

# Compute the integrated result for each 'a' and 'x' pair
integrated_results = -np.cos(2 * a_grid * x_grid) / (4 * a_grid)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(a_grid, x_grid, integrated_results, cmap='viridis')
ax.set_xlabel('a')
ax.set_ylabel('x')
ax.set_zlabel('Integrated Result')

plt.show()
