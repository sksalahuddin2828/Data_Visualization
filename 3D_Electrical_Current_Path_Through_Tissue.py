import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
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

# (d) Calculate temperature increase using specific heat capacity of tissue
specific_heat_tissue = 3500  # J/kg°C
temperature_increase = energy_dissipated / (mass * specific_heat_tissue)

# Display results
print("Charge passed:", charge, "C")
print("Voltage applied:", voltage, "V")
print("Resistance:", resistance, "ohms")
print("Temperature increase:", temperature_increase, "°C")

# Create a DataFrame for visualization
data = {'Parameter': ['Charge Passed', 'Voltage Applied', 'Resistance', 'Temperature Increase'],
        'Value': [charge, voltage, resistance, temperature_increase]}
df = pd.DataFrame(data)

# Create an interactive bar plot using Plotly Express
fig_bar = px.bar(df, x='Parameter', y='Value', title='Electrical Parameters and Temperature Increase')
fig_bar.update_traces(marker_color='blue')

# Display interactive bar plot
fig_bar.show()

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

# Generating 3D data for current path
num_points = 100
x = np.random.rand(num_points) * cube_size
y = np.random.rand(num_points) * cube_size
z = np.random.rand(num_points) * cube_size

# Create 3D scatter plot using Plotly Express
fig_3d = px.scatter_3d(x=x, y=y, z=z, title='Electrical Current Path Through Tissue')
fig_3d.update_traces(marker=dict(size=4, color='blue'))

# Display 3D scatter plot
fig_3d.show()
