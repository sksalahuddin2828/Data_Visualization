import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data (replace with your actual data)
emfx_values = [0.5, 0.7, 0.8, 0.6, 0.9]
emfs_values = [1.0, 1.2, 1.1, 1.3, 1.4]
Rx_values = [2.0, 2.2, 2.5, 2.1, 2.4]
Rs_values = [1.5, 1.7, 1.6, 1.8, 1.9]

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(emfx_values, emfs_values, Rx_values, c=Rs_values, cmap='viridis')

# Customize the plot (labels, title, etc.)
ax.set_xlabel('emfx')
ax.set_ylabel('emfs')
ax.set_zlabel('Rx')
ax.set_title('3D Scatter Plot of emfx, emfs, Rx, and Rs')

# Show the plot
plt.show()


import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data (replace with your actual data)
emfx_values = [0.5, 0.7, 0.8, 0.6, 0.9]
emfs_values = [1.0, 1.2, 1.1, 1.3, 1.4]
Rx_values = [2.0, 2.2, 2.5, 2.1, 2.4]
Rs_values = [1.5, 1.7, 1.6, 1.8, 1.9]

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(emfx_values, emfs_values, Rx_values, c=Rs_values, cmap='viridis')

# Customize the plot (labels, title, etc.)
ax.set_xlabel('emfx')
ax.set_ylabel('emfs')
ax.set_zlabel('Rx')
ax.set_title('3D Scatter Plot of emfx, emfs, Rx, and Rs')

# Add a color bar to represent Rs values
cbar = plt.colorbar(scatter)
cbar.set_label('Rs')

# Show the plot
plt.show()
