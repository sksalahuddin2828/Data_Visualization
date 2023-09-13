import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
B = 0.100  # Magnetic field strength in Tesla
v = 4.00e6  # Speed in m/s
d = 0.01  # Separation between plates in meters

# Part (a) - Calculate the electric field strength
q = sp.symbols('q')
eqn = sp.Eq(q * v, B * q * d)
electric_field = sp.solve(eqn, q)[0]

# Part (b) - Calculate the voltage between plates
voltage = electric_field * d

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot electric field lines
x = np.linspace(-0.02, 0.02, 20)
y = np.linspace(-0.02, 0.02, 20)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)
U = np.ones_like(X) * electric_field
V = np.zeros_like(X)
W = np.zeros_like(X)
ax.quiver(X, Y, Z, U, V, W, length=0.005, normalize=True, color='b', label='Electric Field')

# Plot magnetic field lines
phi = np.linspace(0, 2 * np.pi, 100)
r = np.linspace(0, 0.02, 100)
R, Phi = np.meshgrid(r, phi)
X = R * np.cos(Phi)
Y = R * np.sin(Phi)
Z = np.zeros_like(X)
U = np.zeros_like(X)
V = np.zeros_like(X)
W = np.ones_like(X) * B
ax.quiver(X, Y, Z, U, V, W, length=0.005, normalize=True, color='r', label='Magnetic Field')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Electric and Magnetic Fields')
ax.legend()

# Show the visualization
plt.show()

# Print the results
print(f"(a) Electric field strength needed: {electric_field:.2e} N/C")
print(f"(b) Voltage between plates: {voltage:.2f} V")
