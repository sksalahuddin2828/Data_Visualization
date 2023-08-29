import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
voltage = 120  # Volts
current = 0.01  # Amperes (10 mA)
voltage_across_person = 0  # Since the person doesn't feel it

# Calculate minimum resistance
resistance = voltage / current

# Create a range of resistance values for visualization
resistance_range = np.linspace(0.01, 1000, 100)
voltage_range = resistance_range * current

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the curve
ax.plot(resistance_range, voltage_range, np.zeros_like(resistance_range), label='Voltage vs. Resistance')
ax.scatter([resistance], [voltage_across_person], [0], color='red', marker='o', label='Minimum Resistance')

# Add labels and title
ax.set_xlabel('Resistance (Ohms)')
ax.set_ylabel('Voltage (Volts)')
ax.set_zlabel('Current (Amperes)')
ax.set_title('Minimum Resistance Calculation')

# Add a legend
ax.legend()

# Show the plot
plt.show()
