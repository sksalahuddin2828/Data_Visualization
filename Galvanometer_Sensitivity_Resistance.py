import numpy as np
import sympy as sp

# Given values
galvanometer_resistance = 25.0  # Ω
galvanometer_sensitivity = 50.0e-6  # A
full_scale_reading = 300e-3  # A

# Define the resistance to be found as a symbol
R = sp.Symbol('R', positive=True, real=True)

# Calculate the total resistance of the ammeter (R_total)
R_total = 1 / (1 / galvanometer_resistance + 1 / R)

# Set up the equation for full-scale reading
equation = sp.Eq(full_scale_reading, galvanometer_sensitivity / (galvanometer_resistance + R_total))

# Solve for R
solution = sp.solve(equation, R)

if solution:
    print(f"The required resistance in parallel: {solution[0]} Ω")
else:
    print("No valid solution found.")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure
fig = plt.figure()

# Create a 3D subplot
ax = fig.add_subplot(111, projection='3d')

# Plot a surface to represent the equation
R_values = np.linspace(0.01, 200, 100)  # Values of R
full_scale_readings = np.linspace(0.01, 0.4, 100)  # Full-scale readings
R_values, full_scale_readings = np.meshgrid(R_values, full_scale_readings)
Z = galvanometer_sensitivity / (galvanometer_resistance + 1 / (1 / galvanometer_resistance + 1 / R_values))

# Create a surface plot
ax.plot_surface(R_values, full_scale_readings, Z, cmap='viridis')

# Label axes
ax.set_xlabel('Resistance (R)')
ax.set_ylabel('Full-Scale Reading (A)')
ax.set_zlabel('Current (A)')

# Add a color bar
cbar = fig.colorbar(ax.plot_surface(R_values, full_scale_readings, Z, cmap='viridis'), ax=ax, pad=0.1)

# Show the plot
plt.show()
