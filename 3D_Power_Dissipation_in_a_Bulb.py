import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
voltage_source = 120  # V
wire_resistance = 0.400  # Ω
bulb_power_nominal = 75.0  # W
current_total = 15.0  # A

# Create a symbolic variable for current through the bulb
current_bulb = sp.symbols('I_bulb')

# Calculate the bulb resistance using Ohm's Law
bulb_resistance = voltage_source / current_bulb

# Calculate the power dissipated by the bulb
bulb_power = current_bulb**2 * bulb_resistance

# Solve for current through the bulb
eq = sp.Eq(current_total, current_bulb)
solutions = sp.solve(eq, current_bulb)

if solutions:
    power_dissipated = bulb_power.subs(current_bulb, solutions[0])
    print(f"Power dissipated by the bulb: {power_dissipated} W")
else:
    print("No valid solution found for current through the bulb.")

# Generate data for 3D visualization
current_range = np.linspace(0.01, 20, 100)
resistance_range = voltage_source / current_range
power_range = current_range**2 * resistance_range

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(current_range, resistance_range, power_range, c='r', marker='o')

# Add labels and title
ax.set_xlabel('Current (A)')
ax.set_ylabel('Resistance (Ω)')
ax.set_zlabel('Power (W)')
ax.set_title('Power Dissipation in a Bulb')

# Show the 3D plot
plt.show()
