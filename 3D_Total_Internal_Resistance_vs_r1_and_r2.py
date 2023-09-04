import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate all possible combinations of r1 and r2
r1_values = np.array([0.1, 0.2, 0.3])
r2_values = np.array([0.1, 0.2, 0.3])
r1_values, r2_values = np.meshgrid(r1_values, r2_values)

# Calculate rtot for each combination
rtot_values = 1 / (1 / r1_values + 1 / r2_values)

# Flatten the arrays to create a 1D array
r1_values = r1_values.flatten()
r2_values = r2_values.flatten()
rtot_values = rtot_values.flatten()

# Create the 3D scatter plot
ax.scatter(r1_values, r2_values, rtot_values, c=rtot_values, cmap='viridis')

# Label axes and add a title
ax.set_xlabel('r1')
ax.set_ylabel('r2')
ax.set_zlabel('rtot')
plt.title('Total Internal Resistance vs. r1 and r2')

# Show colorbar for rtot values
cbar = plt.colorbar(ax.scatter(r1_values, r2_values, rtot_values, cmap='viridis'))
cbar.set_label('rtot')

# Show the plot
plt.show()
