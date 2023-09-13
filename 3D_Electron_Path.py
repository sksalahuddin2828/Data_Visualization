import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

v_electron = 6.00e7  # Speed of the electron in m/s
B_earth = 5.00e-5  # Strength of Earth's magnetic field in T
d = 0.01  # Separation between plates in meters

# Calculate the charge of an electron
e = 1.602e-19  # Elementary charge in coulombs

# Calculate the mass of an electron
m_electron = 9.109e-31  # Mass of an electron in kg

# Calculate the required electric field strength using the formula: F_electric = F_magnetic
# F_electric = q * E, F_magnetic = q * v * B_earth
# Setting them equal gives E = v * B_earth
E_required = v_electron * B_earth

# Calculate the voltage using the formula: V = E * d
V = E_required * d

# Create a 3D plot to visualize the electron's motion
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the electron's path
t = np.linspace(0, 1e-6, 1000)  # Time in seconds
x = v_electron * t  # X position
y = np.zeros_like(t)  # Y position (perpendicular to Earth's field)
z = np.zeros_like(t)  # Z position

# Plot the path
ax.plot(x, y, z, label='Electron Path', lw=2)

# Add labels and legend
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.legend()

# Show the plot
plt.show()

print(f"(a) Required electric field strength: {E_required:.2e} N/C")
print(f"(b) Voltage applied: {V:.2f} V")
