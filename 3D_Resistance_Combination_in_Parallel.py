import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Constants
R1 = 75.0e3  # 75.0-kΩ resistor
R2 = 1.00e6  # 1.00-MΩ voltmeter

# (b) Resistance of the combination in parallel
R_combination = 1 / (1/R1 + 1/R2)

# (c) Percent increase in current
V1 = 1.0  # Voltage across 75.0-kΩ resistor (assuming 1 Volt)
I1 = V1 / R1
V2 = 1.0  # Voltage across combination (keeping it the same)
I2 = V2 / R_combination
percent_increase_in_current = ((I2 - I1) / I1) * 100

# (d) Percentage decrease in voltage
I3 = 1.0  # Current through the combination (keeping it the same)
V3 = I3 * R_combination
percent_decrease_in_voltage = ((V1 - V3) / V1) * 100

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Resistance values
R1_values = np.linspace(1e3, 1e6, 100)
R2_values = np.linspace(1e3, 1e6, 100)
R1_values, R2_values = np.meshgrid(R1_values, R2_values)
R_combination_values = 1 / (1/R1_values + 1/R2_values)

# Plot the 3D surface
ax.plot_surface(np.log10(R1_values), np.log10(R2_values), np.log10(R_combination_values), cmap='viridis')

# Add labels
ax.set_xlabel('Log10(R1)')
ax.set_ylabel('Log10(R2)')
ax.set_zlabel('Log10(R_combination)')

# Show the plot
plt.title('Resistance Combination in Parallel')
plt.show()

# Print results
print(f'(b) Resistance of the combination: {R_combination:.2f} Ω')
print(f'(c) Percent increase in current: {percent_increase_in_current:.2f}%')
print(f'(d) Percentage decrease in voltage: {percent_decrease_in_voltage:.2f}%')
