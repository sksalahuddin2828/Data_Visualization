import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sympy as sp

# Define the values
R1 = 1.00  # Ohms
R2 = 2.00  # Ohms
R3 = 3.00  # Ohms
V_total = 12.0  # Volts

# Calculate total resistance
R_total = 1 / (1/R1 + 1/R2 + 1/R3)

# Calculate total current using Ohm's law
I_total = V_total / R_total

# Calculate IR drop in R1
V1 = I_total * R1

# Create a 3D plot for visualization
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Numerical values for x-axis
x_values = [1, 2, 3]

# Plot a point for each resistor with custom labels
resistor_labels = ['R1', 'R2', 'R3']
ax.scatter(x_values, [0, 0, 0], [0, 0, 0], c='b', marker='o', s=100)

# Plot a line representing total resistance
ax.plot([0, 4], [0, 0], [0, V_total], c='g', linestyle='--', linewidth=2, label='Total Resistance')

# Plot lines connecting resistors to the total resistance
for i in range(3):
    ax.plot([x_values[i], 4], [0, 0], [0, V1 if i == 0 else 0], c='r', linestyle='-', linewidth=2)

# Add labels and title
ax.text(4, 0, V_total, 'Total Voltage: {} V'.format(V_total), fontsize=12, verticalalignment='bottom', horizontalalignment='left')
ax.text(4, 0, V1, 'IR drop in R1: {:.2f} V'.format(V1), fontsize=12, verticalalignment='bottom', horizontalalignment='left')

# Set custom labels for x-axis
ax.set_xticks(x_values)
ax.set_xticklabels(resistor_labels)

# Set axis labels
ax.set_xlabel('Resistors')
ax.set_ylabel('Y')
ax.set_zlabel('Voltage (V)')

# Show the plot
plt.legend()
plt.title('3D Visualization of Resistors in Combination')
plt.show()
