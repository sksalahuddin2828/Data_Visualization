import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import torch
import matplotlib.pyplot as plt
from scipy.constants import e

# Given data
current = 10.0  # A
time = 5.00e-3  # seconds
energy_dissipated = 500  # J
mass = 8.00  # kg

# (a) Calculate charge passed
charge = current * time

# (b) Calculate voltage applied
voltage = energy_dissipated / charge

# (c) Calculate resistance
resistance = voltage / current

# (d) Calculate temperature increase using specific heat capacity of tissue (Assuming ~3500 J/kg°C)
specific_heat_tissue = 3500  # J/kg°C
temperature_increase = energy_dissipated / (mass * specific_heat_tissue)

# Display results
print("Charge passed:", charge, "C")
print("Voltage applied:", voltage, "V")
print("Resistance:", resistance, "ohms")
print("Temperature increase:", temperature_increase, "°C")

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a wireframe cube representing affected tissue
cube_size = 2  # arbitrary size
cube = np.array([
    [0, 0, 0],
    [cube_size, 0, 0],
    [0, cube_size, 0],
    [cube_size, cube_size, 0],
    [0, 0, cube_size],
    [cube_size, 0, cube_size],
    [0, cube_size, cube_size],
    [cube_size, cube_size, cube_size]
])
edges = [
    [0, 1], [0, 2], [1, 3], [2, 3],
    [4, 5], [4, 6], [5, 7], [6, 7],
    [0, 4], [1, 5], [2, 6], [3, 7]
]
for edge in edges:
    ax.plot(cube[edge, 0], cube[edge, 1], cube[edge, 2], color='b')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Affected Tissue')

# Show the plot
plt.show()
