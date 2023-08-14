import plotly.graph_objects as go
import numpy as np
import pandas as pd

theta_vals = np.linspace(0, 2 * np.pi, 100)
cos_squared_vals = np.cos(theta_vals)**2
sin_squared_vals = np.sin(theta_vals)**2
two_cos_squared_minus_one_vals = 2 * cos_squared_vals - 1

data = {'Theta': theta_vals,
        'cos^2(θ)': cos_squared_vals,
        'sin^2(θ)': sin_squared_vals,
        '2cos^2(θ) - 1': two_cos_squared_minus_one_vals}

df = pd.DataFrame(data)

# Create traces
traces = []
for column in df.columns[1:]:
    trace = go.Scatter(x=df['Theta'], y=df[column], mode='lines', name=column)
    traces.append(trace)

# Create layout
layout = go.Layout(
    title='Trigonometric Identity Visualization',
    xaxis=dict(title='θ'),
    yaxis=dict(title='Value'),
    legend=dict(x=0.02, y=0.98),
    xaxis_showgrid=True,
    yaxis_showgrid=True
)

# Create figure
fig = go.Figure(data=traces, layout=layout)

# Show the interactive plot
fig.show()
