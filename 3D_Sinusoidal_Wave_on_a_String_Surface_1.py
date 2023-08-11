import numpy as np
import plotly.graph_objs as go

# Given values
ms = 0.070  # kg
Ls = 2.00   # m
FT = 90.00  # N
A = 0.040   # m
f = 60      # Hz

# Calculating angular frequency
omega = 2 * np.pi * f

# Generating the wave profile
x = np.linspace(0, Ls, 100)
t = np.linspace(0, 1, 100)
X, T = np.meshgrid(x, t)
Y = A * np.sin(omega * T) * np.sin(np.pi * X / Ls)

# Create the surface plot
surface_eq1 = go.Surface(x=X, y=T, z=Y, colorscale='Viridis', opacity=0.7)
layout_eq1 = go.Layout(scene=dict(aspectratio=dict(x=1, y=1, z=0.7)))
fig_eq1 = go.Figure(data=[surface_eq1], layout=layout_eq1)
fig_eq1.update_layout(title='Sinusoidal Wave on a String - Surface 1')

# Display the plot
fig_eq1.show()
