import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ipywidgets import widgets
from IPython.display import display

# Create a pandas DataFrame to store data
num_points = 100
alpha_vals = np.linspace(0, np.pi/2, num_points)
beta_vals = np.linspace(0, np.pi/2, num_points)
alpha_mesh, beta_mesh = np.meshgrid(alpha_vals, beta_vals)
gamma_mesh = np.arcsin((np.sin(alpha_mesh) * np.sin(beta_mesh)) / np.sin(np.pi - alpha_mesh - beta_mesh))
df = pd.DataFrame({'alpha': alpha_mesh.ravel(), 'beta': beta_mesh.ravel(), 'gamma': gamma_mesh.ravel()})

# Create a plotly figure
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

# Create 3D surface plot
surface_trace = go.Surface(
    x=df['alpha'].values.reshape((num_points, num_points)),
    y=df['beta'].values.reshape((num_points, num_points)),
    z=df['gamma'].values.reshape((num_points, num_points)),
    colorscale='Viridis'
)
fig.add_trace(surface_trace)

# Set layout
fig.update_layout(
    title='Law of Sines 3D Visualization',
    scene=dict(
        xaxis_title='Angle α',
        yaxis_title='Angle β',
        zaxis_title='Angle γ'
    )
)

# Display the interactive visualization
display(fig)
