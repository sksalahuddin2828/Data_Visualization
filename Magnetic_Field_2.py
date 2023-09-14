import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

diameter = 2.50  # meters
radius = diameter / 2
velocity = 6.00  # m/s
earth_magnetic_field = 5.00e-5  # T

# Hall voltage formula
hall_voltage = velocity * earth_magnetic_field * radius

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a circle representing the water main
theta = np.linspace(0, 2 * np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.zeros_like(x)

ax.plot(x, y, z, label='Water Main', color='blue')

# Create arrows to represent the magnetic field along the x-axis
arrow_length = 1.5 * diameter
arrow_x = np.array([arrow_length, 0])
arrow_y = np.array([0, 0])
arrow_z = np.array([0, 0])

ax.quiver(*arrow_x, *arrow_y, *arrow_z, color='red', label='Magnetic Field')

# Set axis labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.show()

print(f'Hall Voltage: {hall_voltage:.4f} Volts')
