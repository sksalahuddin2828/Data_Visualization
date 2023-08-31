import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Problem values
resistors_series = [786, 20.3]
resistors_parallel = [786, 20.3]

# Total resistance for series
total_resistance_series = sum(resistors_series)

# Total resistance for parallel
total_resistance_parallel = 1 / sum(1 / r for r in resistors_parallel)

print("Total Resistance (Series):", total_resistance_series)
print("Total Resistance (Parallel):", total_resistance_parallel)

# Create a meshgrid of resistor values
R1_values = np.linspace(1, 1000, 100)
R2_values = np.linspace(1, 100, 100)
R1, R2 = np.meshgrid(R1_values, R2_values)

# Calculate total resistance for each combination
total_resistances = 1 / (1/R1 + 1/R2)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(R1, R2, total_resistances, cmap='viridis')

# Add labels and title
ax.set_xlabel('Resistor 1')
ax.set_ylabel('Resistor 2')
ax.set_zlabel('Total Resistance')
ax.set_title('Total Resistance Surface')

plt.show()
