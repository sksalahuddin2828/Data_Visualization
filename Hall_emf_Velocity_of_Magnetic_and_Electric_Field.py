import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
B = 0.5  # Magnetic field strength (Tesla)
v = 2.0  # Velocity of charges (m/s)
l = 1.0  # Width of the conductor (m)

# Calculate Hall emf (ε)
epsilon = B * l * v

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create vectors for velocity, magnetic field, and electric field
origin = np.array([0, 0, 0])
velocity_vector = np.array([v, 0, 0])
magnetic_field_vector = np.array([0, 0, B])
electric_field_vector = np.array([0, epsilon / l, 0])

# Plot vectors
ax.quiver(*origin, *velocity_vector, color='r', label='Velocity')
ax.quiver(*origin, *magnetic_field_vector, color='b', label='Magnetic Field')
ax.quiver(*origin, *electric_field_vector, color='g', label='Electric Field (ε)')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot limits
ax.set_xlim([0, max(v, B) + 1])
ax.set_ylim([0, max(v, B) + 1])
ax.set_zlim([0, max(v, B) + 1])

# Add legend
ax.legend()

# Show the plot
plt.show()

# Print the calculated Hall emf
print(f'Hall emf (ε) = {epsilon} V')
