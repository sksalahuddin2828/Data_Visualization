import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given parameters
resistance_between_hands = 10.0e3  # 10.0 kΩ
voltage_supply = 20.0e3  # 20.0 kV

# Create a range of internal resistance values
internal_resistance_values = np.linspace(0, 5e3, 100)  # Vary internal resistance from 0 to 5000 Ω

# Calculate current through the body for each internal resistance value
current_values = voltage_supply / (resistance_between_hands + internal_resistance_values)

# Calculate power dissipated in the body for each internal resistance value
power_values = current_values**2 * (resistance_between_hands + internal_resistance_values)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the relationship between internal resistance, current, and power
ax.scatter(internal_resistance_values, current_values, power_values, c='b', marker='o')

# Label the axes
ax.set_xlabel('Internal Resistance (Ω)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Power (W)')

# Set the title
ax.set_title('Effect of Internal Resistance on Current and Power')

plt.show()
