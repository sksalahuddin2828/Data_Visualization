import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

battery_voltage = 12.0  # V
internal_resistance_battery = 0.0100  # Ω
starter_motor_resistance = 0.0500  # Ω
corroded_resistance = 0.0900  # Ω

total_resistance = internal_resistance_battery + starter_motor_resistance
current = battery_voltage / total_resistance
print(f"Current to the motor: {current:.4f} A")

voltage_applied = current * starter_motor_resistance
print(f"Voltage applied to the motor: {voltage_applied:.4f} V")

power = current * voltage_applied
print(f"Power supplied to the motor: {power:.4f} W")

# Create a range of corroded resistances
corroded_resistances = np.linspace(0.0100, 0.1000, 100)

# Calculate current, voltage, and power for each corroded resistance
currents = battery_voltage / (internal_resistance_battery + corroded_resistances)
voltages = currents * starter_motor_resistance
powers = currents * voltages

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the results in 3D space
ax.plot(corroded_resistances, currents, powers)

# Label axes and add a title
ax.set_xlabel('Corroded Resistance (Ω)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Power (W)')
ax.set_title('Power vs. Corroded Resistance')

# Show the plot
plt.show()
