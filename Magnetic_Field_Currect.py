# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Define variables
I = 2.0  # Current in Amperes
B = np.array([0, 0, 1])  # Magnetic field vector
l = 1.0  # Length of conductor in meters
theta_deg = 30  # Angle between I and B in degrees

# Convert theta to radians
theta_rad = np.radians(theta_deg)

# Calculate the magnetic force using the formula
F = I * l * np.cross(B, np.array([np.sin(theta_rad), 0, np.cos(theta_rad)]))

# Print the result
print("Magnetic Force (F):", F)

# Create a 3D visualization of the magnetic field and current
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the magnetic field vector
ax.quiver(0, 0, 0, B[0], B[1], B[2], color='b', label='Magnetic Field (B)')

# Plot the current vector
ax.quiver(0, 0, 0, np.sin(theta_rad), 0, np.cos(theta_rad), color='r', label='Current (I)')

ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add a legend
ax.legend()

# Show the plot
plt.show()
