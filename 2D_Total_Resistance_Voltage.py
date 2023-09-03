import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the resistances (you can change these values)
R1 = 2
R2 = 3
R3 = 4

# Calculate the total resistance
total_resistance = R1 + R2 + R3

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define a range of current values
current_values = np.linspace(0.1, 5, 100)

# Calculate voltage for each current value
voltage_values = total_resistance * current_values

# Plot the 3D surface
ax.plot(current_values, R1 * current_values, voltage_values, label='R1')
ax.plot(current_values, R2 * current_values, voltage_values, label='R2')
ax.plot(current_values, R3 * current_values, voltage_values, label='R3')

ax.set_xlabel('Current (I)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Power (P)')

# Add legend
ax.legend()

# Show the plot
plt.show()
