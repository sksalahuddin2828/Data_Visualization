import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Create a meshgrid of x and y values
x_vals = np.linspace(-1, 1, 100)
y_vals = np.linspace(-1, 1, 100)
x_mesh, y_mesh = np.meshgrid(x_vals, y_vals)

# Calculate the z values based on the equation
z_mesh = np.arccos(x_mesh) - (-1 / (1 - x_mesh**2)**0.5)

# Create a Pandas DataFrame for the meshgrid data
data = pd.DataFrame({
    'x': x_mesh.flatten(),
    'y': y_mesh.flatten(),
    'z': z_mesh.flatten()
})

# Create a Plotly 3D scatter plot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])

scatter = go.Scatter3d(
    x=data['x'],
    y=data['y'],
    z=data['z'],
    mode='markers',
    marker=dict(
        size=4,
        colorscale='Viridis',
        opacity=0.8
    )
)

fig.add_trace(scatter)
fig.update_layout(scene=dict(aspectmode="cube"))
fig.update_layout(title='Creative 3D Visualization using Plotly and Pandas')
fig.update_layout(scene=dict(zaxis_title='Z', xaxis_title='X', yaxis_title='Y'))

fig.show()
