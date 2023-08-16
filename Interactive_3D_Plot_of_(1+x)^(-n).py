import numpy as np
import plotly.graph_objects as go

x_vals = np.linspace(-1, 1, 100)
n_vals = np.linspace(0.1, 5, 100)
X, N = np.meshgrid(x_vals, n_vals)
Z = (1 + X)**(-N)

fig = go.Figure(data=[go.Surface(x=X, y=N, z=Z)])
fig.update_layout(title='Interactive 3D Plot of (1+x)^(-n)',
                  scene=dict(xaxis_title='x', yaxis_title='n', zaxis_title='(1+x)^(-n)'))
fig.show()


import pandas as pd

data = {'x': x_vals, 'n': n_vals}
df = pd.DataFrame(data)

# Adding a calculated column based on the equation
df['result'] = (1 + df['x']) ** (-df['n'])

# Create a scatter plot
scatter_fig = df.plot.scatter(x='x', y='result', c='n', colormap='viridis',
                              title='Scatter Plot of (1+x)^(-n)', xlabel='x', ylabel='(1+x)^(-n)')

# Create a line plot
line_fig = df.plot.line(x='x', y='result', title='Line Plot of (1+x)^(-n)', xlabel='x', ylabel='(1+x)^(-n)')

# Display the plots
scatter_fig.get_figure().show()
line_fig.get_figure().show()
