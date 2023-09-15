import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Define variables
I = 2.0  # Current in Amperes
l = 1.0  # Length of conductor in meters
theta_deg = 30  # Angle between I and B in degrees

# Convert theta to radians
theta_rad = np.radians(theta_deg)

# Magnetic field vector
B = np.array([0, 0, 1])

# Calculate the magnetic force using the formula
F = I * l * np.cross(B, np.array([np.sin(theta_rad), 0, np.cos(theta_rad)]))

# Create a Pandas DataFrame for displaying the calculation results
data = {'Parameter': ['Current (I)', 'Length (l)', 'Angle (θ)', 'Magnetic Force (F)'],
        'Value': [I, l, f'{theta_deg}°', F]}
df = pd.DataFrame(data)

# Create an interactive 3D visualization of the magnetic field and current vectors using Plotly
fig = go.Figure()

# Add the magnetic field vector
fig.add_trace(go.Scatter3d(x=[0, B[0]], y=[0, B[1]], z=[0, B[2]], mode='lines+markers', name='Magnetic Field (B)'))

# Add the current vector
current_vector = I * np.array([np.sin(theta_rad), 0, np.cos(theta_rad)])
fig.add_trace(go.Scatter3d(x=[0, current_vector[0]], y=[0, current_vector[1]], z=[0, current_vector[2]],
                           mode='lines+markers', name='Current (I)'))

# Set axis labels
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Add a title
fig.update_layout(title='Magnetic Field and Current Visualization')

# Create an interactive table to display the calculation results
table = go.Figure(data=[go.Table(header=dict(values=['Parameter', 'Value']),
                                 cells=dict(values=[df['Parameter'], df['Value']]))])

# Customize the table layout
table.update_layout(title='Calculation Results', height=150)

# Display the interactive 3D visualization and the table
fig.show()
table.show()
