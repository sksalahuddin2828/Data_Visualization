import numpy as np
import matplotlib.pyplot as plt

# Define constants
q = 1.6e-19  # Charge in Coulombs
v = np.array([1, 0, 0])  # Velocity vector (m/s)
B = np.array([0, 0, 1])  # Magnetic field vector (T)

# Calculate the force
theta = np.pi / 4  # Angle between v and B (45 degrees)
F = q * np.cross(v, B)  # Cross product for force calculation

# Create a 3D visualization of the vectors
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors
ax.quiver(0, 0, 0, v[0], v[1], v[2], color='b', label='Velocity')
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='r', label='Magnetic Field')
ax.quiver(0, 0, 0, F[0], F[1], F[2], color='g', label='Force')

# Set axis limits
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.show()
