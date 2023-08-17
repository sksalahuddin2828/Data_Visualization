import sympy as sp
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define Symbol and Function
x = sp.symbols('x')
f_x = sp.sin(x)  # Example function

# Define the Function af(x) = a * f(x)
a = sp.symbols('a')
af_x = a * f_x

# Calculate the Second Derivative of af(x)
second_derivative = sp.diff(af_x, x, 2)

# Numeric Functions for Visualization
f_numeric = sp.lambdify(x, af_x.subs(a, 10), 'numpy')
second_derivative_numeric = sp.lambdify(x, second_derivative.subs(a, 10), 'numpy')

# Create DataFrames for Original Function and Second Derivative
x_vals = np.linspace(-10, 10, 400)
df_af = pd.DataFrame({'x': x_vals, 'af(x)': f_numeric(x_vals)})
df_second_derivative = pd.DataFrame({'x': x_vals, 'Second Derivative': second_derivative_numeric(x_vals)})

# Create Subplots
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

# Add Traces for Original Function and Second Derivative
fig.add_trace(go.Scatter(x=df_af['x'], y=df_af['af(x)'], mode='lines', name='$af(x)$'), row=1, col=1)
fig.add_trace(go.Scatter(x=df_second_derivative['x'], y=df_second_derivative['Second Derivative'], mode='lines', name='$\\frac{d^2}{dx^2}(af(x))$', line=dict(color='red')), row=2, col=1)

# Customize Layout
fig.update_layout(
    title='Visualization of $af(x)$ and $\\frac{d^2}{dx^2}(af(x))$ using Plotly',
    xaxis_title='x',
    xaxis2_title='x',
    yaxis_title='y',
    yaxis2_title='y',
    height=800,
    width=800,
)

# Show Plot
fig.show()
