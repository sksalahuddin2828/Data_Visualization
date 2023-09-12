# Import necessary libraries
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define constants
velocity = 4.00e3  # m/s
magnetic_field_strength = 1.25  # T
magnetic_force = 1.40e-16  # N
electron_charge = -1.602e-19  # C (charge of an electron)

# Calculate the angle using sympy
angle_symbolic = sp.asin(magnetic_force / (electron_charge * velocity * magnetic_field_strength))

# Convert the angle to degrees
angle_degrees = sp.deg(angle_symbolic)

# Print the results
print(f"Angle (radians): {angle_symbolic}")
print(f"Angle (degrees): {angle_degrees}")

# Create a 3D visualization of the electron's motion
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define a time range for the motion (adjust as needed)
time_range = np.linspace(0, 1e-7, 1000)

# Calculate the trajectory
x = velocity * time_range
y = np.zeros_like(x)  # Initialize y as an array of zeros
z = np.zeros_like(x)  # Initialize z as an array of zeros

# Plot the trajectory
ax.plot(x, y, z, label='Electron Path')

# Customize the plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

# Save or display the 3D plot
plt.savefig("electron_motion.png")  # Save the plot as an image
plt.show()  # Display the plot
