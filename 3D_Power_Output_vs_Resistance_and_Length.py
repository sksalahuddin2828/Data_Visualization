import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import matplotlib.pyplot as plt
import torch
import sklearn
import scipy

# Given values
power_output = 1000  # 1.00 kW in watts
voltage = 120  # Volts

# Calculate resistance using P = V^2 / R
resistance = voltage**2 / power_output
print("Resistance needed:", resistance, "ohms")

# Given values
cross_sectional_area_mm2 = 500  # mm^2
cross_sectional_area_m2 = cross_sectional_area_mm2 * 1e-6  # Convert to m^2
operating_temperature_C = 500  # Celsius
rho_20 = 1.5e-6  # Resistivity of Nichrome at 20°C in ohm*m

# Calculate resistance at operating temperature
alpha = 0.0004  # Temperature coefficient of resistivity
resistivity_operating = rho_20 * (1 + alpha * (operating_temperature_C - 20))
resistance_operating = resistivity_operating * (1 / cross_sectional_area_m2)
print("Resistance at operating temperature:", resistance_operating, "ohms")

# Calculate length using R = ρ * (L / A)
length = resistance_operating * cross_sectional_area_m2 / resistivity_operating
print("Length of Nichrome wire:", length, "meters")

# Given value
initial_voltage = 120  # Volts

# Calculate initial current and power using P = VI
initial_current = initial_voltage / resistance_operating
initial_power = initial_voltage * initial_current
print("Initial power drawn:", initial_power, "watts")

from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid of resistance and length values
resistance_values = np.linspace(0.1, 100, 50)
length_values = np.linspace(0.01, 10, 50)
resistance_mesh, length_mesh = np.meshgrid(resistance_values, length_values)
power_mesh = (initial_voltage ** 2) / resistance_mesh

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(resistance_mesh, length_mesh, power_mesh, cmap='viridis')
ax.set_xlabel('Resistance (ohms)')
ax.set_ylabel('Length (m)')
ax.set_zlabel('Power (W)')
ax.set_title('Power Output vs Resistance and Length')
plt.show()
