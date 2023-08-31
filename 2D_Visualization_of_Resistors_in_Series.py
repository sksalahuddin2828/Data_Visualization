import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given resistances
total_resistance = 0.500e6  # 0.500 MΩ
first_resistance = 900e3     # 900 kΩ

# Calculate the second resistance in series
second_resistance = total_resistance - first_resistance

print("Second Resistance:", second_resistance, "Ω")

# Generate values for the first and second resistors
first_resistor_values = np.linspace(0, 1e6, 100)  # Vary from 0 to 1 MΩ
second_resistor_values = total_resistance - first_resistor_values

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the values
ax.plot(first_resistor_values, second_resistor_values, total_resistance)

# Set labels
ax.set_xlabel('First Resistor (Ω)')
ax.set_ylabel('Second Resistor (Ω)')
ax.set_zlabel('Total Resistance (Ω)')

plt.show()
