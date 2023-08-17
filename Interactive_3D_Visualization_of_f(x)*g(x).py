import numpy as np
import plotly.graph_objs as go

# Generate data for f(x) and g(x)
x_vals = np.linspace(-10, 10, 100)
f_vals = np.sin(x_vals)
g_vals = np.exp(-0.1 * x_vals) * np.cos(x_vals)

# Create a meshgrid for 3D visualization
X, Y = np.meshgrid(x_vals, x_vals)
Z = f_vals[np.newaxis, :] * g_vals[:, np.newaxis]

# Create a 3D surface plot using Plotly
surface_plot = go.Surface(x=X, y=Y, z=Z, colorscale='Viridis')

layout = go.Layout(
    scene=dict(
        xaxis_title='x',
        yaxis_title='f(x)',
        zaxis_title='f(x) * g(x)'
    ),
    title='Interactive 3D Visualization using Plotly'
)

fig = go.Figure(data=[surface_plot], layout=layout)
fig.show()

import pandas as pd

# Create a DataFrame with random data
data = {'x': x_vals, 'f(x)': f_vals, 'g(x)': g_vals}
df = pd.DataFrame(data)

# Display the first few rows of the DataFrame
print(df.head())
