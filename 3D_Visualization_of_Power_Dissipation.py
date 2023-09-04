import numpy as np
import sympy as sp

# Given values
emf = 12.0  # EMF in volts
R_load = 1.0  # Load resistance in ohms
r = 0.5  # Internal resistance in ohms

# Calculate current
I = emf / (R_load + r)

# Calculate terminal voltage
V = emf - I * r

# Calculate power dissipated by the load
P_load = I**2 * R_load

# Print the results
print(f"Current (I): {I} A")
print(f"Terminal Voltage (V): {V} V")
print(f"Power Dissipated by Load (P_load): {P_load} W")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data points for I, V, and P_load
I_values = np.linspace(0, 20, 100)
V_values = emf - I_values * r
P_load_values = I_values**2 * R_load

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(I_values, V_values, P_load_values, c=I_values, cmap='viridis')

# Set labels and title
ax.set_xlabel('Current (I)')
ax.set_ylabel('Terminal Voltage (V)')
ax.set_zlabel('Power Dissipated by Load (P_load)')
ax.set_title('3D Visualization of Power Dissipation')

# Show the plot
plt.show()
