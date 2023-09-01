import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given resistor values
resistor_values = [36.0, 50.0, 700.0]

# Calculate all possible combinations of resistor values
combinations = []
for i in range(2**len(resistor_values)):
    combination = []
    for j in range(len(resistor_values)):
        if (i >> j) & 1:
            combination.append(resistor_values[j])
    if len(combination) == len(resistor_values):  # Check if all resistors are used
        combinations.append(combination)

# Calculate the equivalent resistance for each combination
equivalent_resistances = []
for combination in combinations:
    equivalent_resistance = np.sum(1 / np.array(combination))
    equivalent_resistances.append(equivalent_resistance)

# Find the largest and smallest equivalent resistances
largest_resistance = max(equivalent_resistances)
smallest_resistance = min(equivalent_resistances)

# Print the results
print(f"Largest Resistance: {largest_resistance} ohms")
print(f"Smallest Resistance: {smallest_resistance} ohms")

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extract values for the 3D plot
x = [comb[0] for comb in combinations]
y = [comb[1] for comb in combinations]
z = equivalent_resistances

# Plot the equivalent resistances in 3D
ax.scatter(x, y, z, c=z, cmap='viridis')
ax.set_xlabel('Resistor 1 (ohms)')
ax.set_ylabel('Resistor 2 (ohms)')
ax.set_zlabel('Equivalent Resistance (ohms)')

plt.show()
