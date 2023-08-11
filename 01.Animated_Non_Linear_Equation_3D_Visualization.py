import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Define the non-linear equation
def nonlinear_equation(x):
    return 4 * x**2 + 5 * x + 3

# Generate x values
x = np.linspace(-10, 10, 400)

# Calculate corresponding y values using the equation
y = nonlinear_equation(x)

# Create a DataFrame for the data
data = pd.DataFrame({'x': x, 'y': y})

# Create animated plot using Plotly
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])
scatter = fig.add_trace(go.Scatter(x=data['x'], y=data['y'], mode='lines', name='y = 4x^2 + 5x + 3'))

# Create animation frames
frames = [go.Frame(data=[go.Scatter(x=data['x'][:i], y=data['y'][:i], mode='lines', name='y = 4x^2 + 5x + 3')],
                   name=str(i)) for i in range(2, len(x), 5)]

# Add frames to the animation
fig.frames = frames

# Define animation buttons
animation_buttons = [
    {'label': 'Play', 'method': 'animate', 'args': [None, {'frame': {'duration': 50, 'redraw': True}, 'fromcurrent': True}]},
    {'label': 'Pause', 'method': 'animate', 'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'after'}]}
]

# Update layout for animation
fig.update_layout(updatemenus=[{'buttons': animation_buttons, 'direction': 'left', 'pad': {'r': 10, 't': 87}, 'showactive': False, 'type': 'buttons', 'x': 0.1, 'xanchor': 'right', 'y': 0, 'yanchor': 'top'}],
                  title='Animated Non-linear Equation Visualization',
                  xaxis_title='x',
                  yaxis_title='y',
                  xaxis=dict(range=[-10, 10]),
                  yaxis=dict(range=[min(y), max(y)]),
                  showlegend=False)

# Show the plot
fig.show()
