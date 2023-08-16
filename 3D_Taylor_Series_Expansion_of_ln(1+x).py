import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sympy as sp

# Define the symbolic variable
x = sp.Symbol('x')

# Define the equation
equation = sp.ln(1 + x)

# Calculate the Taylor series expansion of the equation
taylor_series = sp.series(equation, x, n=10).removeO()

# Convert the symbolic expression to a numeric function
taylor_func = sp.lambdify(x, taylor_series, 'numpy')

# Generate x values
x_vals = np.linspace(-1, 1, 500)

# Calculate y values using the Taylor function
y_vals = taylor_func(x_vals)

# Create a DataFrame for easy data manipulation
data = pd.DataFrame({'x': x_vals, 'Taylor Series': y_vals, 'ln(1+x)': np.log(1 + x_vals)})

# Create an interactive plot using Plotly
fig = go.Figure()
fig.add_trace(go.Scatter(x=data['x'], y=data['Taylor Series'], name='Taylor Series', mode='lines'))
fig.add_trace(go.Scatter(x=data['x'], y=data['ln(1+x)'], name='ln(1+x)', mode='lines'))

fig.update_layout(title='Taylor Series Expansion of ln(1+x)',
                  xaxis_title='x', yaxis_title='y')
fig.update_xaxes(range=[-1, 1])  # Adjust x-axis range

# Add interactive legend
fig.update_layout(updatemenus=[{'active': 0,
                                'buttons': [{'label': 'All',
                                             'method': 'relayout',
                                             'args': ['showlegend', True]},
                                            {'label': 'Taylor Series',
                                             'method': 'relayout',
                                             'args': ['showlegend', [True, False]]},
                                            {'label': 'ln(1+x)',
                                             'method': 'relayout',
                                             'args': ['showlegend', [False, True]]}]}])

# Add annotations
fig.add_annotation(text='Interactive Legend:', x=-0.9, y=4.5, showarrow=False)

# Show plot
fig.show()
