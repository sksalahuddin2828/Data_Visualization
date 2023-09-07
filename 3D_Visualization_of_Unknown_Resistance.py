import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
import torch
from sklearn.linear_model import LinearRegression
from scipy.optimize import fsolve

# Given data
galvanometer_sensitivity = 50e-6  # in Amperes
galvanometer_resistance = 25.0  # in Ohms
full_scale_voltage = 3000.0  # in Volts

# Unknown resistance (to be calculated)
unknown_resistance = sp.symbols('R')

# Using Ohm's law to calculate current through the galvanometer
current_galvanometer = full_scale_voltage / galvanometer_resistance

# Using the sensitivity, calculate the current corresponding to full-scale deflection
full_scale_current = galvanometer_sensitivity

# Setup the equation: current_galvanometer = full_scale_voltage / (unknown_resistance + galvanometer_resistance)
equation = sp.Eq(current_galvanometer, full_scale_voltage / (unknown_resistance + galvanometer_resistance))

# Solve for unknown_resistance
solution = sp.solve(equation, unknown_resistance)

# Convert the solution to a numeric value
unknown_resistance_value = solution[0].evalf()

# Create a 3D plot of resistance vs. sensitivity vs. full-scale voltage
sensitivity_values = np.linspace(1e-6, 100e-6, 100)
voltage_values = np.linspace(1, 10000, 100)
sensitivity_grid, voltage_grid = np.meshgrid(sensitivity_values, voltage_values)
resistance_grid = voltage_grid / (sensitivity_grid * full_scale_voltage)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(sensitivity_grid, voltage_grid, resistance_grid, cmap='viridis')
ax.set_xlabel('Sensitivity (A/V)')
ax.set_ylabel('Full-Scale Voltage (V)')
ax.set_zlabel('Unknown Resistance (Ohms)')
plt.title('3D Visualization of Unknown Resistance')
plt.show()
