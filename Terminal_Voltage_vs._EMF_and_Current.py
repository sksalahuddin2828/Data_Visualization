import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
emf = 1.54  # EMF of the cell in volts
internal_resistance = 0.100  # Internal resistance of the cell in ohms
current = 2.00  # Current supplied by the cell in amperes

# (a) Calculate the terminal voltage
voltage_drop = internal_resistance * current
terminal_voltage = emf - voltage_drop

# (b) Calculate the electrical power produced by the cell
power_produced = emf * current

# (c) Calculate the power delivered to the load (circuit)
power_delivered_to_load = terminal_voltage * current

# Display results
print("(a) Terminal Voltage:", terminal_voltage, "V")
print("(b) Power Produced by the Cell:", power_produced, "W")
print("(c) Power Delivered to the Load:", power_delivered_to_load, "W")

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of points
x = np.linspace(0, emf, 100)
y = np.linspace(0, current, 100)
X, Y = np.meshgrid(x, y)

# Calculate terminal voltage for each combination of EMF and current
Z = X - internal_resistance * Y

# Plot the 3D surface
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and a title
ax.set_xlabel('EMF (V)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Terminal Voltage (V)')
ax.set_title('Terminal Voltage vs. EMF and Current')

# Show the plot
plt.show()
