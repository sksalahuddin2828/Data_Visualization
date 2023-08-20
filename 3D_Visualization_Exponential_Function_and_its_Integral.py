import numpy as np
import plotly.graph_objects as go
from sympy import symbols, exp
from plotly.subplots import make_subplots

# Define symbolic variables
x, a = symbols('x a')
c = symbols('c')

# Define the expression
expression = exp(a * x)

# Integrate the expression
integral_result = (1 / a) * exp(a * x) + c

# Create a grid of 'a' and 'x' values
a_values = np.linspace(0.1, 2, 50)
x_values = np.linspace(0, 2, 100)
a_grid, x_grid = np.meshgrid(a_values, x_values)

# Evaluate the integrated result for each 'a' value and 'x' value
integrated_results = np.empty_like(a_grid)
for i in range(a_values.shape[0]):
    for j in range(x_grid.shape[1]):  # Use x_grid.shape[1] instead of x_values.shape[0]
        integrated_results[i, j] = integral_result.subs({a: a_values[i], x: x_grid[i, j], c: 0}).evalf()

# Create an interactive surface plot using Plotly
fig = go.Figure()

# Add surface plot for the integral result
fig.add_trace(go.Surface(z=integrated_results, x=a_grid, y=x_grid))

# Update layout
fig.update_layout(scene=dict(xaxis_title='a', yaxis_title='x', zaxis_title='Integrated Result'))

# Show the interactive plot
fig.show()

import pandas as pd

# Create a DataFrame from the grids
data = {'a': a_grid.flatten(), 'x': x_grid.flatten(), 'integrated_result': integrated_results.flatten()}
df = pd.DataFrame(data)

# Create an interactive 3D scatter plot using Plotly
scatter_plot = go.Figure(data=[go.Scatter3d(x=df['a'], y=df['x'], z=df['integrated_result'], mode='markers')])
scatter_plot.update_layout(scene=dict(xaxis_title='a', yaxis_title='x', zaxis_title='Integrated Result'))

# Show the interactive scatter plot
scatter_plot.show()
