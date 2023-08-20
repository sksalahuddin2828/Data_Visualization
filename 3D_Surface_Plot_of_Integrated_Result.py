import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a and x values for 3D plot
a_values_3d = np.linspace(0.1, 2, 50)
x_values_3d = np.linspace(0, 2, 50)
a_grid_3d, x_grid_3d = np.meshgrid(a_values_3d, x_values_3d)

# Calculate integrated results for 3D plot
integrated_results_3d = (np.exp(a_grid_3d * x_grid_3d) / (a_grid_3d**2)) * (a_grid_3d * x_grid_3d - 1)

# Create 3D plot
fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')
ax_3d.plot_surface(a_grid_3d, x_grid_3d, integrated_results_3d)

# Set labels and title
ax_3d.set_xlabel('a')
ax_3d.set_ylabel('x')
ax_3d.set_zlabel('Integrated Result')
ax_3d.set_title('3D Surface Plot of Integrated Result')

# Show the plot
plt.show()
