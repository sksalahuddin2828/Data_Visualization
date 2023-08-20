# Interactive Visualization using Plotly

import numpy as np
import plotly.graph_objects as go

# Create a grid of 'a' and 'x' values
a_values = np.linspace(0.1, 2, 50)
x_values = np.linspace(0, 1, 50)
a_grid, x_grid = np.meshgrid(a_values, x_values)

# Compute the integrated result for each 'a' and 'x' pair
integrated_results = -np.cos(2 * a_grid * x_grid) / (4 * a_grid)

# Create an interactive 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(z=integrated_results, x=a_grid, y=x_grid)])
fig.update_layout(scene=dict(xaxis_title='a', yaxis_title='x', zaxis_title='Integrated Result'))

fig.show()

# Creating a DataFrame and Visualization

import pandas as pd

# Create a DataFrame from the grids
data = {'a': a_grid.flatten(), 'x': x_grid.flatten(), 'integrated_result': integrated_results.flatten()}
df = pd.DataFrame(data)

# Visualization using Scatter3d plot from Plotly
scatter_plot = go.Figure(data=[go.Scatter3d(x=df['a'], y=df['x'], z=df['integrated_result'],
                                             mode='markers')])
scatter_plot.update_layout(scene=dict(xaxis_title='a', yaxis_title='x', zaxis_title='Integrated Result'))

scatter_plot.show()
