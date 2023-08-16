import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sympy as sp

# Define the symbolic variable
x = sp.Symbol('x')

# Define the equation
equation = sp.ln(1 + x)

# Generate x values
x_vals = np.linspace(-1, 1, 500)

# Convert the symbolic expression to a numeric function
ln_func = sp.lambdify(x, equation, 'numpy')

# Create an interactive figure with subplots
fig = make_subplots(rows=1, cols=2, subplot_titles=('Taylor Series Expansion', 'Error Comparison'))

terms_slider = 5  # Default value
terms_slider_step = 1

def update(terms=5):
    taylor_series = sp.series(equation, x, n=terms).removeO()
    taylor_func = sp.lambdify(x, taylor_series, 'numpy')
    y_vals_taylor = taylor_func(x_vals)
    y_vals_actual = ln_func(x_vals)

    # Clear existing traces
    fig.data = []

    fig.add_trace(go.Scatter(x=x_vals, y=y_vals_taylor, mode='lines', name='Taylor Series'), row=1, col=1)
    fig.update_xaxes(title_text='x', row=1, col=1)
    fig.update_yaxes(title_text='y', row=1, col=1)

    # Calculate the error
    error = np.abs(y_vals_taylor - y_vals_actual)

    fig.add_trace(go.Scatter(x=x_vals, y=error, mode='lines', name='Error'), row=1, col=2)
    fig.update_xaxes(title_text='x', row=1, col=2)
    fig.update_yaxes(title_text='Error', row=1, col=2)

    # Update layout
    fig.update_layout(title='Interactive Visualization of ln(1+x) Taylor Series Expansion',
                      showlegend=False)

update(terms_slider)  # Initial plot

fig.show()
