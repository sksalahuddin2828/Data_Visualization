import numpy as np

# Resistances in ohms
resistor_values = [1e2, 2.5e3, 4e3]

# Calculate total resistance in series
total_resistance_series = np.sum(resistor_values)

# Calculate total resistance in parallel
total_resistance_parallel = 1 / np.sum(1 / np.array(resistor_values))

print(f"Total Resistance in Series: {total_resistance_series:.2f} ohms")
print(f"Total Resistance in Parallel: {total_resistance_parallel:.2f} ohms")

# Answer: Total Resistance in Series: 6600.00 ohms
#         Total Resistance in Parallel: 93.90 ohms

#----------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Resistances in ohms
resistor_values = [1e2, 2.5e3, 4e3]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Scatter plot for resistors
x_positions = np.arange(len(resistor_values))
y_positions = np.zeros(len(resistor_values))
z_values = resistor_values

ax.scatter(x_positions, y_positions, z_values, c='b', s=100, marker='s')  # Use 's' for squares

# Label the axes
ax.set_xlabel('Resistor')
ax.set_ylabel('Unused Dimension')
ax.set_zlabel('Resistance (Ohms)')
ax.set_title('Resistors in 3D')

plt.show()
