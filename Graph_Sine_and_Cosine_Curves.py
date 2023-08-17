import sympy as sp

x = sp.symbols('x')
f = sp.Function('f')(x)
g = sp.Function('g')(x)

expr = f * sp.sin(g) + sp.exp(-x) / (x + 1)
derivative_expr = sp.diff(expr, x)

# Printing the result
print("Expression:", expr)
print("Derivative:", derivative_expr)

import pandas as pd

data = {'x': [1, 2, 3, 4, 5],
        'f_x': [2, 3, 5, 7, 11],
        'g_x': [1, 4, 9, 16, 25]}

df = pd.DataFrame(data)

# Performing operations
df['f_times_g'] = df['f_x'] * df['g_x']
df['f_plus_g'] = df['f_x'] + df['g_x']

# Applying a custom function
def custom_function(row):
    return row['f_x'] ** row['g_x']

df['custom_function_result'] = df.apply(custom_function, axis=1)

# Display the DataFrame
print(df)

import numpy as np
import plotly.express as px

# Create data
x = np.linspace(-2*np.pi, 2*np.pi, 500)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a line plot with interactive features
fig = px.line(x=x, y=[y1, y2], labels={'x': 'X', 'y': 'Y'}, title='Sine and Cosine Curves')
fig.update_layout(legend_title='Functions', legend=dict(x=0, y=1))
fig.update_traces(mode='lines', hoverinfo='y+x')

# Show the interactive plot
fig.show()

# Explanation for symbolic mathematics
print("Expression:", expr)
print("This expression combines a function f(x) with sine of g(x) and the exponential of -x divided by (x + 1).")

# Adding annotations to the Plotly visualization
fig.add_annotation(text='Peak of Sine Curve', x=3, y=1, arrowhead=2)
fig.add_annotation(text='Peak of Cosine Curve', x=-2, y=1, arrowhead=2)
