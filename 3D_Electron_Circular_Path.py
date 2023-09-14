import numpy as np
import pandas as pd
import plotly.express as px

# Constants
velocity = 7.50e6  # m/s
magnetic_field_strength = 1.00e-5  # T
electron_charge = -1.602e-19  # C (charge of an electron)
electron_mass = 9.109e-31  # kg (mass of an electron)

# Calculate the radius of the circular path
radius = (electron_mass * velocity) / (np.abs(electron_charge) * magnetic_field_strength)

# Create a pandas DataFrame to store electron's position data
num_points = 1000
theta = np.linspace(0, 2 * np.pi, num_points)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.zeros_like(x)  # Electron remains at the same altitude

electron_path = pd.DataFrame({'X': x, 'Y': y, 'Z': z})

# Create an interactive 3D plot using Plotly
fig = px.line_3d(electron_path, x='X', y='Y', z='Z', title='Electron Circular Path')
fig.update_traces(line=dict(width=3))
fig.update_layout(scene=dict(aspectmode="cube"))
fig.update_layout(scene=dict(xaxis_title='X position (m)', yaxis_title='Y position (m)', zaxis_title='Altitude (m)'))

# Show the interactive plot
fig.show()
