import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, Eq, solve
import math

# Constants
m_oxygen_16 = 2.66e-26  # Mass of oxygen-16 in kg
q = 1.602e-19  # Charge of ions in coulombs (singly charged)
v = 5.00e6  # Velocity of ions in m/s
B = 1.20  # Magnetic field strength in Tesla
r_symbol = Symbol('r')  # Radius of semicircle

# Mass spectrometer equation for radius of curvature
eqn = Eq((m_oxygen_16 * v) / (q * B), r_symbol)

# Solve for radius of curvature
radius = solve(eqn, r_symbol)[0]

# Calculate the angle subtended by the path separation
angle_rad = (2 * math.asin(1)) / 2  # Half of the semicircle (180 degrees)
angle_deg = math.degrees(angle_rad)

# Calculate the separation between the paths
separation = 2 * radius * math.sin(angle_rad)

# Print the result
print(f"The separation between the paths is {separation:.2f} meters")

# 3D Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a semicircle
theta = np.linspace(0, np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.zeros_like(x)

# Plot the paths of oxygen-16 and oxygen-18 ions
ax.plot(x, y, z, label='Path of Oxygen-16')
ax.plot(x, -y, z, label='Path of Oxygen-18')

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.show()
