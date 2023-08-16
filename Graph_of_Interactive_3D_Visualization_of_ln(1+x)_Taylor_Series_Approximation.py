import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sympy as sp

# Define the symbolic variable
x = sp.Symbol('x')

# Define the equation
equation = sp.ln(1 + x)

# Convert the symbolic expression to a numeric function
ln_func = sp.lambdify(x, equation, 'numpy')

# Generate x values
x_vals = np.linspace(-1, 1, 500)

# Calculate actual ln(1+x) values
y_vals_actual = ln_func(x_vals)

# Create an interactive figure with subplots
fig = make_subplots(rows=1, cols=2, subplot_titles=('Taylor Series Terms', 'Error Comparison'))

def update(terms=5):
    fig.data = []  # Clear existing traces

    taylor_series = sum([sp.diff(equation, x, k).subs(x, 0) / sp.factorial(k) * x**k for k in range(terms)])
    taylor_func = sp.lambdify(x, taylor_series, 'numpy')
    y_vals_taylor = taylor_func(x_vals)

    fig.add_trace(go.Scatter(x=x_vals, y=y_vals_taylor, mode='lines+markers', name='Approximation'), row=1, col=1)
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals_actual, mode='lines', name='Actual ln(1+x)'), row=1, col=1)
    fig.update_xaxes(title_text='x', row=1, col=1)
    fig.update_yaxes(title_text='y', row=1, col=1)
    fig.update_layout(annotations=[dict(text=f'Terms: {terms}', x=0.75, y=1.05, showarrow=False)])

    # Calculate the error
    error = np.abs(y_vals_taylor - y_vals_actual)

    fig.add_trace(go.Bar(x=x_vals, y=error, name='Error'), row=1, col=2)
    fig.update_xaxes(title_text='x', row=1, col=2)
    fig.update_yaxes(title_text='Error', row=1, col=2)

    # Update layout
    fig.update_layout(title='Interactive Visualization of ln(1+x) Taylor Series Approximation',
                      showlegend=True, legend=dict(x=1, y=1))

update(terms=5)  # Initial plot

fig.show()
