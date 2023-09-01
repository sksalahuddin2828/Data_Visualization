import numpy as np

# Constants
voltage = 48.0  # V
resistances_series = np.array([24.0, 96.0])  # Ω
resistances_parallel = 1 / (1 / 24.0 + 1 / 96.0)  # Ω

# Calculate current in series
current_series = voltage / np.sum(resistances_series)

# Calculate current in parallel
current_parallel = voltage / resistances_parallel

# Calculate power in series
power_series = current_series**2 * resistances_series

# Calculate power in parallel
power_parallel = current_parallel**2 * resistances_parallel

print("Series Configuration:")
print(f"Current: {current_series} A")
print(f"Power: {power_series} W")

print("\nParallel Configuration:")
print(f"Current: {current_parallel} A")
print(f"Power: {power_parallel} W")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a 3D plot of the circuit
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Add resistors as 3D lines
ax.plot([0, 0], [0, 0], [0, -1], 'k', lw=3, label='24 Ω Resistor')
ax.plot([0, 0], [0, 0], [-1, -2], 'b', lw=3, label='96 Ω Resistor')

# Add labels and annotations
ax.text(0, 0, -0.5, 'Battery', fontsize=12, color='r')
ax.text(0, 0, -1.5, 'Series Circuit', fontsize=14, color='g')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add legend
ax.legend()

# Show the plot
plt.show()
