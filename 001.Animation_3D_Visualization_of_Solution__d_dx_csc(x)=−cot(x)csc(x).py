import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from IPython.display import display, clear_output
import time

# Define the range of x values
x_vals = np.linspace(0.01, np.pi - 0.01, 300)  # Avoiding singularity at x = 0 and x = pi

# Calculate the equation and its solution
equation_vals = -np.cos(x_vals) / (np.sin(x_vals) ** 2)
solution_vals = -1 / np.sin(x_vals)

# Calculate the derivative of the solution
derivative_vals = (1 / np.sin(x_vals)) * np.cos(x_vals)

# Create a Pandas DataFrame for the data
data = pd.DataFrame({
    'x': x_vals,
    'Equation': equation_vals,
    'Solution': solution_vals,
    'Derivative': derivative_vals
})

# Create Plotly figure
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Add traces for equation, solution, and derivative
equation_trace = go.Scatter(
    x=data['x'],
    y=data['Equation'],
    mode='lines',
    name='Equation: $-\cos(x) / \sin^2(x)$',
    line=dict(color='blue')
)

solution_trace = go.Scatter(
    x=data['x'],
    y=data['Solution'],
    mode='lines',
    name='Solution: $-1 / \sin(x)$',
    line=dict(color='green', dash='dash')
)

derivative_trace = go.Scatter(
    x=data['x'],
    y=data['Derivative'],
    mode='lines',
    name='Derivative: $\\frac{\\cos(x)}{\\sin(x)}$',
    line=dict(color='red', dash='dot')
)

fig.add_trace(equation_trace)
fig.add_trace(solution_trace)
fig.add_trace(derivative_trace)

# Customize layout
fig.update_layout(
    title='Creative Animated Visualization using Plotly and Pandas',
    xaxis_title='x',
    yaxis_title='y',
    legend=dict(x=0.02, y=0.98),
    template='plotly_dark'
)

# Create the animation
animation_frames = []

for i in range(len(data)):
    frame_data = go.Frame(
        data=[
            go.Scatter(x=data['x'][:i], y=data['Equation'][:i], mode='lines', line=dict(color='blue')),
            go.Scatter(x=data['x'][:i], y=data['Solution'][:i], mode='lines', line=dict(color='green', dash='dash')),
            go.Scatter(x=data['x'][:i], y=data['Derivative'][:i], mode='lines', line=dict(color='red', dash='dot'))
        ],
        traces=[0, 1, 2],
        name=f'Frame {i}'
    )
    animation_frames.append(frame_data)

# Add frames to the figure and create animations
fig.frames = animation_frames

# Add play and pause buttons
fig.update_layout(updatemenus=[{
    'type': 'buttons',
    'showactive': False,
    'buttons': [
        {
            'label': 'Play',
            'method': 'animate',
            'args': [None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]
        },
        {
            'label': 'Pause',
            'method': 'animate',
            'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}]
        }
    ]
}])

# Display the animation
fig.show()
