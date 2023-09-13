import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Constants
mass_oxygen_ion = 2.66e-26  # kg
velocity = 5.00e6  # m/s
magnetic_field = 1.20  # T
radius = 0.231  # m
electron_charge = 1.602e-19  # C

# Calculate charge of the oxygen-16 ion
charge = (mass_oxygen_ion * velocity) / (radius * magnetic_field)

# Calculate the ratio of charge to electron charge
charge_ratio = charge / electron_charge

# Calculate radius for an electron
# Rearrange the formula: r = (m * v) / (q * B)
radius_electron = (mass_oxygen_ion * velocity) / (electron_charge * magnetic_field)

# Visualization
# Create a 3D plot to visualize the circular path
theta = np.linspace(0, 2 * np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.zeros_like(theta)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Circular Path')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Create a bar chart to show the charge ratio
plt.figure()
plt.bar(['Charge of Oxygen Ion', 'Charge of Electron'], [charge, electron_charge])
plt.xlabel('Particle')
plt.ylabel('Charge (C)')
plt.title('Charge Comparison')

# Show the results
print(f"(a) Charge of the oxygen-16 ion: {charge} C")
print(f"(b) Charge ratio to an electron: {charge_ratio}")
print(f"(c) Radius of circular path for an electron: {radius_electron} m")

plt.show()
