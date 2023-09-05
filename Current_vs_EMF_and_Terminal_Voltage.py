import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Given data
emf = 12.0  # V
terminal_voltage = 15.0  # V
current = 8.00  # A

# Calculate internal resistance (R)
R = (emf - terminal_voltage) / current

# Display the internal resistance
print(f"Internal Resistance (R): {R:.2f} ohms")

# Visualize the problem in 3D
# Create a grid of values for emf and terminal voltage
emf_values = np.linspace(0, 20, 100)
terminal_voltage_values = np.linspace(0, 20, 100)
emf_values, terminal_voltage_values = np.meshgrid(emf_values, terminal_voltage_values)

# Calculate internal resistance for each combination of emf and terminal voltage
current_values = (emf_values - terminal_voltage_values) / R

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(emf_values, terminal_voltage_values, current_values, cmap='viridis')
ax.set_xlabel('EMF (V)')
ax.set_ylabel('Terminal Voltage (V)')
ax.set_zlabel('Current (A)')
ax.set_title('Current vs EMF and Terminal Voltage')

# Show the 3D plot
plt.show()
