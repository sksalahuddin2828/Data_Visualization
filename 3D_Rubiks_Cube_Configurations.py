import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define data for the Rubik's cube
edges = 12
corners = 8
total_cubies = edges + corners

# Plot the corners
corner_positions = np.arange(1, corners + 1)
corner_orientations = np.full(corners, 3)
ax.bar3d(corner_positions, 0, 0, 0.8, 0.8, corner_orientations)

# Plot the edges
edge_positions = np.arange(corners + 1, total_cubies + 1)
edge_orientations = np.full(edges, 2)
ax.bar3d(edge_positions, 0, 0, 0.8, 0.8, edge_orientations)

# Set labels and title
ax.set_xlabel('Cubies')
ax.set_ylabel('Orientation')
ax.set_zlabel('Count')
ax.set_title('Rubik\'s Cube Configurations')

# Show the plot
plt.show()
