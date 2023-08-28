import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given parameters
power = 500  # in watts
voltage = 120  # in volts

# Calculate resistance using R = V^2 / P
resistance = voltage**2 / power

# Calculate peak current using Ohm's law: I = V / R
peak_current = voltage / resistance

# Create a range of voltage and power values for visualization
voltage_range = np.linspace(100, 150, 20)
power_range = np.linspace(300, 700, 20)
voltage_grid, power_grid = np.meshgrid(voltage_range, power_range)
current_grid = voltage_grid / (voltage_grid**2 / power_grid)

# Create a 3D plot
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(voltage_grid, power_grid, current_grid, cmap='viridis')
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Power (W)')
ax.set_zlabel('Current (A)')
ax.set_title('Peak Current of a Room Heater')
plt.show()
