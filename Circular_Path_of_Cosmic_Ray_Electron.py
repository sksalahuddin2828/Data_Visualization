import numpy as np
import matplotlib.pyplot as plt

# Constants
velocity = 7.50e6  # m/s
magnetic_field_strength = 1.00e-5  # T
electron_charge = -1.602e-19  # C (charge of an electron)
electron_mass = 9.109e-31  # kg (mass of an electron)

# Calculate the radius of the circular path using the formula: r = (m * v) / (|q| * B)
radius = (electron_mass * velocity) / (np.abs(electron_charge) * magnetic_field_strength)

# Print the radius
print(f"The radius of the circular path is {radius:.2f} meters")

# Create a circle representing the path
circle = plt.Circle((0, 0), radius, fill=False, color='blue')

# Create a figure and axis
fig, ax = plt.subplots()

# Add the circle to the plot
ax.add_artist(circle)

# Set the aspect ratio to be equal
ax.set_aspect('equal', adjustable='datalim')

# Set plot limits
ax.set_xlim(-1.5 * radius, 1.5 * radius)
ax.set_ylim(-1.5 * radius, 1.5 * radius)

# Add labels and title
ax.set_xlabel('X position (m)')
ax.set_ylabel('Y position (m)')
ax.set_title('Circular Path of Cosmic Ray Electron')

# Show the plot
plt.grid()
plt.show()
