import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Define the range of x and y values
x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
x_mesh, y_mesh = np.meshgrid(x_vals, y_vals)

# Calculate the z values based on the equation
z_mesh = np.abs(np.diff(np.tan(x_mesh), axis=0) - (1 / np.cos(y_mesh[:-1, :]))**2)

# Create a Pandas DataFrame for the meshgrid data
data = pd.DataFrame({
    'x': x_mesh[:-1, :].flatten(),
    'y': y_mesh[:-1, :].flatten(),
    'z': z_mesh.flatten()
})

# Create Plotly 3D surface plot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

surface = go.Surface(
    x=data['x'].values.reshape((99, 100)),  # Correct shape here
    y=data['y'].values.reshape((99, 100)),  # Correct shape here
    z=data['z'].values.reshape((99, 100)),  # Correct shape here
    colorscale='Viridis',
    showscale=True,
)

fig.add_trace(surface)

# Customize layout
fig.update_layout(
    title='Creative Interactive 3D Visualization using Plotly and Pandas',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    template='plotly_dark'
)

# Display the plot
fig.show()
