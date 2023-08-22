import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
angle_deg = 80
r_perp = 98.5  # meters
force_magnitude = 5.0e5  # Newtons

# Calculate torque magnitude
torque_magnitude = -r_perp * force_magnitude

# Convert angle to radians
angle_rad = np.radians(angle_deg)

# Calculate torque vector components
torque_vector = np.array([
    torque_magnitude * np.sin(angle_rad),
    0,
    torque_magnitude * np.cos(angle_rad)
])

# Visualize torque vector
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(0, 0, 0, torque_vector[0], torque_vector[1], torque_vector[2], color='b')
ax.set_xlim([0, torque_vector[0]])
ax.set_ylim([0, torque_vector[1]])
ax.set_zlim([0, torque_vector[2]])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Torque Vector Visualization')
plt.show()
