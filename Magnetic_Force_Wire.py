import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
I = 5.0  # Current in Amperes
B = 0.2  # Magnetic field strength in Tesla
theta = np.pi / 6  # Angle between current and magnetic field (30 degrees)
l = 1.0  # Length of wire in meters

# Calculate the magnetic force
F_magnitude = I * l * B * np.sin(theta)

# Create a vector for the magnetic force
F = np.array([F_magnitude * np.cos(theta), F_magnitude * np.sin(theta), 0])

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a wire segment
wire_points = np.array([[0, 0, 0], [l * np.cos(theta), l * np.sin(theta), 0]])

# Plot the wire segment
ax.plot(wire_points[:, 0], wire_points[:, 1], wire_points[:, 2], 'b', linewidth=3, label='Wire')

# Plot the magnetic force vector
ax.quiver(0, 0, 0, F[0], F[1], F[2], color='r', label='Magnetic Force')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot limits
ax.set_xlim([0, l])
ax.set_ylim([0, l])
ax.set_zlim([0, l])

# Add a legend
ax.legend()

# Show the plot
plt.show()
