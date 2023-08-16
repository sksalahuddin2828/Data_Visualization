import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Generate x values
x_vals = np.linspace(-10, 10, 300)

# Calculate tan(x) and the series approximation
tan_x = np.tan(x_vals)
series_approx = x_vals + (x_vals ** 3) / 3 + (2 * x_vals ** 5) / 15

# Create a DataFrame to store data
data = {'x': x_vals, 'tan(x)': tan_x, 'Series Approx.': series_approx}
df = pd.DataFrame(data)

# Create a Plotly subplot
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter'}, {'type': 'scatter3d'}]])

# Add scatter plot for tan(x) and series approximation
scatter_tan = go.Scatter(x=df['x'], y=df['tan(x)'], mode='lines', name='tan(x)')
scatter_series = go.Scatter(x=df['x'], y=df['Series Approx.'], mode='lines', name='Series Approx.')

# Add scatter3d plot
scatter3d = go.Scatter3d(x=df['x'], y=df['x'], z=df['tan(x)'], mode='lines', name='tan(x)')
scatter3d_series = go.Scatter3d(x=df['x'], y=df['x'], z=df['Series Approx.'], mode='lines', name='Series Approx.')

fig.add_trace(scatter_tan, row=1, col=1)
fig.add_trace(scatter_series, row=1, col=1)
fig.add_trace(scatter3d, row=1, col=2)
fig.add_trace(scatter3d_series, row=1, col=2)

# Update subplot layout
fig.update_layout(title='Comparison of tan(x) and Series Approximation',
                  scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
                  scene2=dict(xaxis_title='x', yaxis_title='x', zaxis_title='f(x)'),
                  width=1000, height=500)

# Show the plot
fig.show()
