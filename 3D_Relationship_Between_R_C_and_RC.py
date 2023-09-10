import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
R = 1000  # Resistance in ohms
RC_max = 1e-2  # Maximum RC time constant in seconds (1.00 × 10^2 μs)

# Create a range of capacitance values
C_values = np.linspace(1e-9, 1e-6, 1000)  # Capacitance range from 1 nF to 1 µF

# Calculate time constant values for each capacitance
RC_values = R * C_values

# Create a 3D plot to visualize the relationship between R, C, and RC
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Color map based on RC values
colors = RC_values

# Scatter plot with color gradient
scatter = ax.scatter(R * np.ones_like(C_values), C_values, RC_values, c=colors, cmap='viridis', marker='o')

ax.set_xlabel('Resistance (ohms)')
ax.set_ylabel('Capacitance (F)')
ax.set_zlabel('RC Time Constant (s)')
ax.set_title('Relationship Between R, C, and RC')

# Highlight the region where RC < RC_max
max_capacitance = np.max(C_values[RC_values < RC_max])
ax.scatter(R, max_capacitance, RC_max, color='red', label=f'Max C: {max_capacitance:.2e} F')

# Add colorbar
cbar = fig.colorbar(scatter)
cbar.set_label('RC Value')

# Add annotations
ax.text(R, max_capacitance, RC_max, f'Max C: {max_capacitance:.2e} F', color='red', fontsize=10, ha='center')

ax.legend()

# Show the plot
plt.show()

# Print the maximum capacitance
print(f"The maximum capacitance (C_max) to satisfy RC < {RC_max:.2e} s is: {max_capacitance:.2e} F")
