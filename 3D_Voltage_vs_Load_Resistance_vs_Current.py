import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
voltage_cell = 1.58  # Volts
internal_resistance = 0.200  # Ohms
current_load = 8.50  # Amperes

# (a) Calculate terminal voltage
terminal_voltage = voltage_cell - current_load * internal_resistance

# (b) Calculate the load resistance using Ohm's law
load_resistance = terminal_voltage / current_load

# (c) Determine what's unreasonable about the results
# We need to check if the calculated values make sense.

unreasonable_results = []
if terminal_voltage < 0:
    unreasonable_results.append("Negative terminal voltage")
if load_resistance < 0:
    unreasonable_results.append("Negative load resistance")
if load_resistance > 100:
    unreasonable_results.append("Load resistance too high (unrealistic)")

# (d) List assumptions that are unreasonable or inconsistent
# Assumptions that may be unreasonable include the constant internal resistance
# and constant voltage of the alkaline cell.

# Print the results and unreasonable findings
print("(a) Terminal Voltage:", terminal_voltage, "Volts")
print("(b) Load Resistance:", load_resistance, "Ohms")
print("(c) Unreasonable Results:", unreasonable_results)

# Create a basic 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define a grid of values for terminal voltage, load resistance, and current
terminal_voltage_vals = np.linspace(0, 2, 100)
load_resistance_vals = np.linspace(0, 10, 100)
current_vals = terminal_voltage_vals / load_resistance_vals

# Create a 3D scatter plot
ax.scatter(terminal_voltage_vals, load_resistance_vals, current_vals, c='r', marker='o')

# Label axes
ax.set_xlabel('Terminal Voltage (V)')
ax.set_ylabel('Load Resistance (Ω)')
ax.set_zlabel('Current (A)')

# Show the plot
plt.show()
