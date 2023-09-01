import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
V = 12.0  # Voltage in volts
headlight_power = 30.0  # Headlight power in watts
starter_power = 2400.0  # Starter power in watts

# Resistance calculations
headlight_resistance = V**2 / headlight_power
starter_resistance = V**2 / starter_power

# Parallel Connection
total_parallel_resistance = 1 / ((1 / headlight_resistance) + (1 / starter_resistance))
parallel_current = V / total_parallel_resistance
parallel_headlight_power = parallel_current**2 * headlight_resistance
parallel_starter_power = parallel_current**2 * starter_resistance

# Series Connection
total_series_resistance = headlight_resistance + starter_resistance
series_current = V / total_series_resistance
series_headlight_power = series_current**2 * headlight_resistance
series_starter_power = series_current**2 * starter_resistance

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

connection_types = ['Parallel', 'Series']
powers = [parallel_headlight_power + parallel_starter_power, series_headlight_power + series_starter_power]

x_pos = np.arange(len(connection_types))
y_pos = np.zeros(len(connection_types))
z_pos = np.zeros(len(connection_types))
dx = dy = 0.5
dz = powers

colors = ['b', 'r']  # Blue for Parallel, Red for Series

ax.bar3d(x_pos, y_pos, z_pos, dx, dy, dz, color=colors, shade=True)

ax.set_xticks(x_pos)
ax.set_xticklabels(connection_types)
ax.set_xlabel('Connection Type')

ax.set_yticks([0])
ax.set_yticklabels(['Power (W)'])
ax.set_ylabel('Measurement')

ax.set_zlabel('Power (W)')
ax.set_title('Power Consumption in Different Connection Types')

plt.show()
