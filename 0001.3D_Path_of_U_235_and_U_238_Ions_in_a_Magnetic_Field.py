import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sympy as sp
import pandas as pd
import plotly.graph_objects as go

# Constants
mass_U235 = 3.90e-25  # Mass of uranium-235 ion (kg)
mass_U238 = 3.95e-25  # Mass of uranium-238 ion (kg)
velocity = 3.00e5      # Velocity of ions (m/s)
magnetic_field = 0.250  # Magnetic field strength (T)
charge_U235 = 3        # Charge of uranium-235 ion (e)
charge_U238 = 3        # Charge of uranium-238 ion (e)

# Calculate radius of semicircle path for each ion
radius_U235 = (mass_U235 * velocity) / (charge_U235 * magnetic_field)
radius_U238 = (mass_U238 * velocity) / (charge_U238 * magnetic_field)

# Calculate the separation between their paths when they hit a target
separation = radius_U238 - radius_U235

# Calculate the period and frequency of motion
period_U235 = 2 * np.pi * mass_U235 * radius_U235 / (charge_U235 * velocity)
frequency_U235 = 1 / period_U235

# Symbolic variables and equations
t = sp.Symbol('t', real=True)
angle_U235 = (velocity * t) / radius_U235
angle_U238 = (velocity * t) / radius_U238
x_U235_expr = radius_U235 * sp.cos(angle_U235)
y_U235_expr = radius_U235 * sp.sin(angle_U235)
x_U238_expr = radius_U238 * sp.cos(angle_U238)
y_U238_expr = radius_U238 * sp.sin(angle_U238)

# Lambdify symbolic expressions for numerical calculation
calculate_positions_sym = sp.lambdify(t, (x_U235_expr, y_U235_expr, x_U238_expr, y_U238_expr), 'numpy')

# Time values for animation
time_values = np.linspace(0, 2 * np.pi, 100)

# Calculate positions for U-235 and U-238 separately
x_U235, y_U235, x_U238, y_U238 = calculate_positions_sym(time_values)

# Create DataFrames for position data
position_data_U235 = pd.DataFrame({'Time': time_values, 'X_U235': x_U235, 'Y_U235': y_U235})
position_data_U238 = pd.DataFrame({'Time': time_values, 'X_U238': x_U238, 'Y_U238': y_U238})

# Create an interactive 3D visualization using Plotly
fig = go.Figure()

fig.add_trace(go.Scatter3d(
    x=position_data_U235['X_U235'],
    y=position_data_U235['Y_U235'],
    z=time_values,
    mode='lines+markers',
    name='U-235 Path',
))

fig.add_trace(go.Scatter3d(
    x=position_data_U238['X_U238'],
    y=position_data_U238['Y_U238'],
    z=time_values,
    mode='lines+markers',
    name='U-238 Path',
))

fig.update_layout(
    title='Path of U-235 and U-238 Ions in a Magnetic Field',
    scene=dict(
        xaxis_title='X Position (m)',
        yaxis_title='Y Position (m)',
        zaxis_title='Time (s)',
    ),
)

# Print the separation distance, period, and frequency
print(f"Separation between paths: {separation:.4f} meters")
print(f"Period of U-235 motion: {period_U235:.4f} seconds")
print(f"Frequency of U-235 motion: {frequency_U235:.4f} Hz")

# Additional explanations and theory can be added here as text explanations.

# Show the interactive Plotly visualization
fig.show()
