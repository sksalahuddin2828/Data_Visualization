import numpy as np
import sympy as sp

# Given data
proton_velocity = 5.00e7  # m/s
force = 1.70e-16  # N
angle_deg = 45  # degrees

# Convert angle to radians
angle_rad = np.deg2rad(angle_deg)

# Calculate the magnetic field strength (B)
B = force / (proton_velocity * np.sin(angle_rad))
print(f"Magnetic Field Strength (B): {B} T")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Spherical coordinates for magnetic field direction
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

# Magnetic field direction in spherical coordinates
x = B * np.sin(theta) * np.cos(phi)
y = B * np.sin(theta) * np.sin(phi)
z = B * np.cos(theta)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='viridis')

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Magnetic Field Direction')

plt.show()
