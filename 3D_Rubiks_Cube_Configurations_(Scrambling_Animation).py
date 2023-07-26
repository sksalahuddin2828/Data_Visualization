import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to generate random cube orientations
def generate_random_orientations(count):
    return np.random.randint(0, 3, size=count)

# Function to generate random cube locations
def generate_random_locations(count):
    return np.random.permutation(np.arange(1, count + 1))

# Generate data for corner and edge cubies
corner_cubies = 8
edge_cubies = 12
total_cubies = corner_cubies + edge_cubies

corner_orientations = generate_random_orientations(corner_cubies)
corner_locations = generate_random_locations(corner_cubies)

edge_orientations = generate_random_orientations(edge_cubies)
edge_locations = generate_random_locations(edge_cubies)

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for corner cubies
ax.scatter(corner_locations, corner_orientations, c='red', marker='o', label='Corner Cubies')

# Scatter plot for edge cubies
ax.scatter(edge_locations, edge_orientations, c='blue', marker='^', label='Edge Cubies')

# Set labels and title
ax.set_xlabel('Cubie Location')
ax.set_ylabel('Orientation')
ax.set_zlabel('Cubie Type')
ax.set_title('Rubik\'s Cube Configurations')

# Legend
ax.legend(loc='upper left')

# Animation to showcase cube scrambling
def update_plot(frame):
    # Generate new random orientations and locations
    corner_orientations = generate_random_orientations(corner_cubies)
    corner_locations = generate_random_locations(corner_cubies)

    edge_orientations = generate_random_orientations(edge_cubies)
    edge_locations = generate_random_locations(edge_cubies)

    # Update the scatter plot
    ax.cla()
    ax.scatter(corner_locations, corner_orientations, c='red', marker='o', label='Corner Cubies')
    ax.scatter(edge_locations, edge_orientations, c='blue', marker='^', label='Edge Cubies')
    ax.set_xlabel('Cubie Location')
    ax.set_ylabel('Orientation')
    ax.set_zlabel('Cubie Type')
    ax.set_title('Rubik\'s Cube Configurations (Scrambling Animation)')

# Animate the plot
from matplotlib.animation import FuncAnimation
anim = FuncAnimation(fig, update_plot, frames=20, interval=500)

# To display the animation, you can save it as a GIF or use the following command:
plt.show()
