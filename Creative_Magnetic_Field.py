import numpy as np
import pandas as pd
import plotly.graph_objs as go

# Define parameters
diameter = 2.50  # meters
radius = diameter / 2
velocity = 6.00  # m/s
earth_magnetic_field = 5.00e-5  # T

# Calculate Hall voltage
hall_voltage = velocity * earth_magnetic_field * radius

# Create a DataFrame for the magnetic field
df_magnetic_field = pd.DataFrame({'x': [0, 2 * radius], 'y': [0, 0], 'z': [0, 0], 'magnitude': [0, 1]})

# Create a 3D scatter plot for the magnetic field
trace_magnetic_field = go.Scatter3d(
    x=df_magnetic_field['x'],
    y=df_magnetic_field['y'],
    z=df_magnetic_field['z'],
    mode='markers',
    marker=dict(size=df_magnetic_field['magnitude'] * 10, color='red'),
    name='Magnetic Field'
)

# Create a DataFrame for the water main
theta = np.linspace(0, 2 * np.pi, 100)
df_water_main = pd.DataFrame({'x': radius * np.cos(theta), 'y': radius * np.sin(theta), 'z': np.zeros_like(theta)})

# Create a 3D scatter plot for the water main
trace_water_main = go.Scatter3d(
    x=df_water_main['x'],
    y=df_water_main['y'],
    z=df_water_main['z'],
    mode='lines',
    marker=dict(size=5, color='blue'),
    name='Water Main'
)

# Create a DataFrame for the Hall voltage arrow
df_hall_voltage_arrow = pd.DataFrame({'x': [0], 'y': [0], 'z': [0], 'vx': [0], 'vy': [0], 'vz': [hall_voltage]})

# Create a 3D vector arrow for the Hall voltage
trace_hall_voltage_arrow = go.Cone(
    x=df_hall_voltage_arrow['x'],
    y=df_hall_voltage_arrow['y'],
    z=df_hall_voltage_arrow['z'],
    u=df_hall_voltage_arrow['vx'],
    v=df_hall_voltage_arrow['vy'],
    w=df_hall_voltage_arrow['vz'],
    colorscale='greens',
    sizemode='absolute',
    sizeref=0.1,
    showscale=True,
    name='Hall Voltage'
)

# Create the layout for the 3D plot
layout = go.Layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Z'),
    ),
    showlegend=True,
)

# Create the 3D plot figure
fig = go.Figure(data=[trace_magnetic_field, trace_water_main, trace_hall_voltage_arrow], layout=layout)

# Show the plot
fig.show()
