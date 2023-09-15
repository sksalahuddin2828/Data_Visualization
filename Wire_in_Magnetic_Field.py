import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
current = 30.0  # Amperes
force = 2.16  # Newtons
wire_length = 0.04  # meters (4.00 cm)

# Calculate the average field strength (B) using the formula: B = F / (I * L)
average_field_strength = force / (current * wire_length)

# Create a 3D visualization of the wire and magnetic field
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the wire as a line segment
wire_start = np.array([0, 0, 0])
wire_end = np.array([0, 0, wire_length])

# Plot the wire
ax.plot([wire_start[0], wire_end[0]], [wire_start[1], wire_end[1]], [wire_start[2], wire_end[2]], 'b', label='Wire')

# Define the magnetic field between the poles
field_strength = average_field_strength  # Assuming uniform field strength
field_start = np.array([-0.02, 0, 0])
field_end = np.array([0.02, 0, 0])

# Plot the magnetic field
ax.quiver(field_start[0], field_start[1], field_start[2], field_end[0], field_end[1], field_end[2], color='r', label='Magnetic Field')

# Set labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Wire in Magnetic Field')
ax.legend()

# Display the plot
plt.show()

# Print the average field strength
print(f"Average Field Strength (B): {average_field_strength} Tesla")
