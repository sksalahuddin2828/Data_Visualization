import plotly.graph_objects as go
import numpy as np

# Create a meshgrid for x and m values
x_vals = np.linspace(0.1, 5, 100)
m_vals = np.linspace(-2, 2, 100)
X, M = np.meshgrid(x_vals, m_vals)

# Calculate the z values (integral results)
Z = X**M

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(x=X, y=M, z=Z)])
fig.update_layout(title='Interactive 3D Integral Visualization',
                  scene=dict(xaxis_title='x', yaxis_title='m', zaxis_title='Integral Result'))

# Show the interactive plot
fig.show()
