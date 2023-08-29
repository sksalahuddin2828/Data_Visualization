import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt

# Given data
power = 1.44e3  # in watts
resistance = 0.100  # in ohms

# Calculate current using P = I^2 * R
current = np.sqrt(power / resistance)

# Calculate voltage using Ohm's Law: V = I * R
voltage = current * resistance

# Display the results
print(f"Current: {current:.2f} A")
print(f"Voltage: {voltage:.2f} V")

from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D subplot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data points
current_range = np.linspace(0.01, 10, 100)
resistance_range = np.linspace(0.01, 2, 100)
current_range, resistance_range = np.meshgrid(current_range, resistance_range)
voltage_range = current_range * resistance_range

# Create the 3D surface plot
surface = ax.plot_surface(current_range, resistance_range, voltage_range, cmap='viridis')

# Add labels and title
ax.set_xlabel('Current (A)')
ax.set_ylabel('Resistance (Ω)')
ax.set_zlabel('Voltage (V)')
ax.set_title('Voltage as a Function of Current and Resistance')

# Add color bar
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

# Show the plot
plt.show()
