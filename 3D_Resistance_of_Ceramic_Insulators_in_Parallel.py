import numpy as np

# Given data
resistance_per_insulator = 1.00e9  # Ohms
number_of_insulators = 100

# Total resistance in parallel is given by the reciprocal of the sum of reciprocals
total_resistance = 1 / np.sum(1 / resistance_per_insulator)

print("Total resistance to ground:", total_resistance, "Ohms")

voltage = 240e3  # Volts

# Using Ohm's law to calculate current through the insulators
current = voltage / total_resistance

# Power dissipated = I^2 * R
power_dissipated = current ** 2 * total_resistance

print("Power dissipated:", power_dissipated, "Watts")

power_transmitted = 5.00e2  # Watts

fraction_dissipated = power_dissipated / power_transmitted

print("Fraction of power dissipated:", fraction_dissipated)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure and a 3D Axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate some data for plotting
resistor_values = np.linspace(0.1e9, 5.0e9, 100)
insulator_counts = np.arange(1, 101)
X, Y = np.meshgrid(insulator_counts, resistor_values)
Z = 1 / (1 / Y * X).T

# Create the 3D surface plot
surface = ax.plot_surface(X, Y, Z, cmap='viridis')

# Add labels and title
ax.set_xlabel('Number of Insulators')
ax.set_ylabel('Resistance per Insulator (Ohms)')
ax.set_zlabel('Total Resistance (Ohms)')
ax.set_title('Resistance of Ceramic Insulators in Parallel')

# Add colorbar
fig.colorbar(surface, ax=ax, label='Total Resistance (Ohms)')

plt.show()
