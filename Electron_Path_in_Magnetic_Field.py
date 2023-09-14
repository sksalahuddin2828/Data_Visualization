import sympy as sp
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# Constants
m = 9.11e-31  # Mass of an electron in kg
v = 6.00e7  # Velocity of the electron in m/s
q = 1.60e-19  # Charge of an electron in C
B = 0.500  # Magnetic field strength in T

# Calculate radius of curvature
r = (m * v) / (q * B)

# Create a pandas DataFrame for clear presentation
data = {
    "Quantity": ["Mass (m)", "Velocity (v)", "Charge (q)", "Magnetic Field (B)", "Radius (r)"],
    "Value": [m, v, q, B, r],
    "Unit": ["kg", "m/s", "C", "T", "m"]
}

df = pd.DataFrame(data)

# 3D Visualization of Electron Path using Plotly
t = np.linspace(0, 2 * np.pi, 100)  # Time points
x = r * np.cos(t)  # X-coordinate
y = r * np.sin(t)  # Y-coordinate
z = t  # Z-coordinate (time)

# Create an interactive 3D plot
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='lines', name='Electron Path')])
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Time'),
                  title='Electron Path in Magnetic Field',
                  showlegend=True)

# Create an interactive table using Plotly
table_data = [go.Table(
    header=dict(values=df.columns),
    cells=dict(values=[df[col] for col in df.columns]))
]

# Show the interactive plot and table
fig.show()
fig2 = go.Figure(data=table_data)
fig2.show()
