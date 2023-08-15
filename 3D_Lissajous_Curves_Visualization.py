import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from ipywidgets import widgets
from IPython.display import display

# Generate data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.cos(Y)

# Create a plotly figure
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])

# Create 3D surface plot
surface_trace = go.Surface(x=X, y=Y, z=Z, colorscale='Viridis')
fig.add_trace(surface_trace)

# Set layout
fig.update_layout(
    title='Creative 3D Visualization using Plotly',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z'
    )
)

# Display the interactive visualization
display(fig)
