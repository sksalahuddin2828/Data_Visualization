import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data Preparation
voltage = 12.0  # Voltage source
resistors = [4, 6, 9]  # Resistor values
current_series = voltage / np.array(resistors)
current_parallel = voltage / resistors[0] + voltage / resistors[1] + voltage / resistors[2]

power_series = current_series ** 2 * np.array(resistors)
power_parallel = current_parallel ** 2 * np.array(resistors)

# Create 3D Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot Series Connection
ax.bar(["R1", "R2", "R3"], power_series, zdir='y', width=0.4, color='b', alpha=0.6, label='Series')

# Plot Parallel Connection
ax.bar(["R1", "R2", "R3"], power_parallel, zdir='y', width=0.4, color='r', alpha=0.6, label='Parallel')

# Add Labels and Legends
ax.set_xlabel('Resistors')
ax.set_ylabel('Power (W)')
ax.set_zlabel('Connection Type')
ax.set_title('Power Dissipation in Series vs. Parallel')

# Show the plot
plt.legend()
plt.show()
