import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
velocity = 7.50e7  # m/s
radius = 0.800  # m

# Calculate the magnetic field strength using the formula: B = (mv) / (qR)
proton_mass = 1.6726219e-27  # kg
proton_charge = 1.60217663e-19  # C

magnetic_field_strength = (proton_mass * velocity) / (proton_charge * radius)

# Print the result
print(f"Magnetic Field Strength: {magnetic_field_strength:.4e} Tesla")

# Create a 3D plot of the proton's circular path
t = np.linspace(0, 2 * np.pi, 1000)
x = radius * np.cos(t)
y = radius * np.sin(t)
z = np.zeros_like(t)  # Since motion is in the xy-plane

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Proton Path', linewidth=2)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Proton Path in Magnetic Field')

plt.legend()
plt.show()
