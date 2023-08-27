import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
voltage = 240  # Voltage in volts
power_north_america = 25.0  # Power in watts

# Calculate resistance using P = V^2 / R
resistance = (voltage ** 2) / power_north_america

# Create a range of resistance values for visualization
resistance_values = np.linspace(1, 100, 100)
voltage_values = np.sqrt(power_north_america * resistance_values)

# Calculate power consumption for each resistance value
power_consumption = (voltage_values ** 2) / resistance_values

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(resistance_values, voltage_values, power_consumption, label='Power Consumption')
ax.set_xlabel('Resistance')
ax.set_ylabel('Voltage')
ax.set_zlabel('Power')
ax.set_title('Power Consumption of Razor')
ax.legend()

# Display the plot
plt.show()
