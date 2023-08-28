import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import torch
import sklearn
import scipy.constants as const
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
voltage = 120  # V
current = 10.0  # A

# Calculate peak power consumption (in watts)
peak_power = voltage * current

# Display the result
print("Peak Power Consumption:", peak_power, "W")

# Create a 3D visualization using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data points
voltage_range = np.linspace(0, 240, 100)
current_range = np.linspace(0, 20, 100)
V, I = np.meshgrid(voltage_range, current_range)
P = V * I

# Plot the 3D surface
ax.plot_surface(V, I, P, cmap='viridis')
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Power (W)')
ax.set_title('Power Consumption of Microwave Oven')
plt.show()
