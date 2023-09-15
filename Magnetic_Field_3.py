import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the magnetic field vector (B) and current vector (I)
B = np.array([0, 0, -1])  # Magnetic field out of the page
I = np.array([0, 0, -1])  # Current downward

# Calculate the magnetic force on the current (F)
F = np.cross(I, B)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the magnetic field vector
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='blue', label='Magnetic Field (B)')

# Plot the current vector
ax.quiver(0, 0, 0, I[0], I[1], I[2], color='red', label='Current (I)')

# Plot the magnetic force vector
ax.quiver(0, 0, 0, F[0], F[1], F[2], color='green', label='Magnetic Force (F)')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set axis limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Add a legend
ax.legend()

# Show the plot
plt.show()
