import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Constants
A = 1.0
k = 2.0
ω = 3.0
ϕ = np.pi / 4.0

# Generate data
x = np.linspace(0, 10, 100)  # Spatial coordinates
t = np.linspace(0, 5, 50)    # Time coordinates

X, T = np.meshgrid(x, t)     # Meshgrid for 3D plot

# Compute wave function
y = A * np.sin(k * X - ω * T + ϕ)

# Additional mathematical expressions
velocity = A * ω * np.cos(k * X - ω * T + ϕ)
acceleration = -A * ω**2 * np.sin(k * X - ω * T + ϕ)

# Create a 3D plot using Plotly
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'surface'}, {'type': 'surface'}]])

# Surface plot for wave function
fig.add_trace(go.Surface(x=X, y=T, z=y, colorscale='viridis'), row=1, col=1)

# Surface plot for velocity
fig.add_trace(go.Surface(x=X, y=T, z=velocity, colorscale='plasma'), row=1, col=2)

# Update layout for 3D visualizations
fig.update_layout(scene=dict(aspectmode="manual", aspectratio=dict(x=1, y=2, z=1)),
                  scene2=dict(aspectmode="manual", aspectratio=dict(x=1, y=2, z=1)))

# Annotations and titles
fig.update_layout(title='Wave Propagation and Velocity in 3D')

fig.show()
