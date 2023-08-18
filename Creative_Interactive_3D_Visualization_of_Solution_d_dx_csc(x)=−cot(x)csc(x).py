import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Define the range of x values
x_vals = np.linspace(0.01, np.pi - 0.01, 300)  # Avoiding singularity at x = 0 and x = pi

# Calculate the equation and its solution
equation_vals = -np.cos(x_vals) / (np.sin(x_vals) ** 2)
solution_vals = -1 / np.sin(x_vals)

# Create a Pandas DataFrame for the data
data = pd.DataFrame({
    'x': x_vals,
    'Equation': equation_vals,
    'Solution': solution_vals
})

# Create Plotly figure with subplots
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Add traces for equation and solution
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

fig.add_trace(equation_trace)
fig.add_trace(solution_trace)

# Highlight important points using annotations
annotations = [
    dict(
        x=np.pi / 2,
        y=1,
        xref="x",
        yref="y",
        text="Singularity at π/2",
        showarrow=True,
        arrowhead=3,
        ax=0,
        ay=-40
    ),
    dict(
        x=np.pi / 4,
        y=-2**0.5,
        xref="x",
        yref="y",
        text="Minimum at π/4",
        showarrow=True,
        arrowhead=3,
        ax=-60,
        ay=0
    )
]

fig.update_layout(annotations=annotations)

# Customize layout
fig.update_layout(
    title='Creative Interactive Visualization using Plotly and Pandas',
    xaxis_title='x',
    yaxis_title='y',
    legend=dict(x=0.02, y=0.98),
    template='plotly_dark'
)

# Display the plot
fig.show()
