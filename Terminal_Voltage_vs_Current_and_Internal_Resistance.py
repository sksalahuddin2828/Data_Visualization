import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Given data
v_battery = 12.0  # V
r_internal = 0.600  # Ohms
current = 10.0  # A

# (a) Calculate terminal voltage
terminal_voltage = v_battery - current * r_internal

# (b) Calculate output voltage of the charger
output_voltage = terminal_voltage + current * r_internal

# Visualization using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a grid of values for current and internal resistance
current_range = np.linspace(0, 15, 100)
resistance_range = np.linspace(0, 1, 100)
current_values, resistance_values = np.meshgrid(current_range, resistance_range)

# Calculate terminal voltage for the grid
terminal_voltage_values = v_battery - current_values * resistance_values

# Plot the surface
ax.plot_surface(current_values, resistance_values, terminal_voltage_values, cmap='viridis')
ax.set_xlabel('Current (A)')
ax.set_ylabel('Internal Resistance (Ohms)')
ax.set_zlabel('Terminal Voltage (V)')
ax.set_title('Terminal Voltage vs Current and Internal Resistance')

plt.show()

# Print the results
print(f'(a) Terminal Voltage: {terminal_voltage:.2f} V')
print(f'(b) Output Voltage of Charger: {output_voltage:.2f} V')
