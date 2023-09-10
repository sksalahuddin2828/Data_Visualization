import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
C = 160e-6  # Capacitance in Farads
V0 = 450  # Initial voltage in Volts
R = 31.2e3  # Resistance in Ohms
mass = 2.50  # Mass of resistor in grams
specific_heat = 1.67  # Specific heat in kJ/kg°C

# (a) Calculate the time constant (τ)
tau = R * C

# (b) Calculate the temperature increase
# Energy dissipated during discharge
energy = 0.5 * C * V0**2

# Convert energy to Joules and calculate temperature increase
energy_joules = energy * 1000  # Convert kJ to J
temperature_increase = energy_joules / (mass / 1000 * specific_heat)  # Convert grams to kg

print("Time Constant (τ):", tau)
print("Temperature Increase:", temperature_increase, "°C")

# Create a grid of time constants and temperature increases
tau_values = np.linspace(0.001, 0.1, 100)  # Adjust the range for better visualization
temp_increases = np.linspace(0, 100, 100)  # Adjust the range for better visualization
tau_values, temp_increases = np.meshgrid(tau_values, temp_increases)
temperature_map = energy_joules / (mass / 1000 * specific_heat) * (1 - np.exp(-tau_values))  # Temperature increase formula

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surface = ax.plot_surface(tau_values, temp_increases, temperature_map, cmap='viridis')
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)  # Add color bar

# Customize the plot
ax.set_xlabel('Time Constant (τ)')
ax.set_ylabel('Temperature Increase (°C)')
ax.set_zlabel('Temperature Map')
ax.set_title('Temperature Increase vs. Time Constant')

# Show the plot
plt.show()
