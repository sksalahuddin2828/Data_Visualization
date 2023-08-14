import numpy as np
import pandas as pd
import sympy as sp
import plotly.graph_objs as go

a_list = [1, 2, 3]
b_list = [2, -1, 4]
c_list = [1, 5, -2]

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # Return None for no real roots
    elif discriminant == 0:
        root = -b / (2*a)
        return root
    else:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        return root1, root2

roots_data = []

for a_val, b_val, c_val in zip(a_list, b_list, c_list):
    roots = solve_quadratic(a_val, b_val, c_val)
    if roots is not None:
        roots_data.append({'a': a_val, 'b': b_val, 'c': c_val, 'roots': roots})

df = pd.DataFrame(roots_data)

# Create an interactive scatter 3D plot using Plotly
scatter_plot = go.Scatter3d(
    x=df['a'],
    y=df['b'],
    z=[r if isinstance(r, float) else r[0] for r in df['roots']],  # Handle both single roots and tuples
    mode='markers',
    marker=dict(size=8, color='red', opacity=0.8),
    name='Real Roots'
)

layout = go.Layout(
    scene=dict(
        xaxis_title='a',
        yaxis_title='b',
        zaxis_title='Roots',
    )
)

scatter_fig = go.Figure(data=[scatter_plot], layout=layout)
scatter_fig.show()

# Symbolic quadratic equation and plot using Plotly Express
x = sp.symbols('x')
equation = x**2 + sp.symbols('b')*x + sp.symbols('c')

equation_values = [equation.subs({sp.symbols('b'): b, sp.symbols('c'): c}) for b, c in zip(b_list, c_list)]

express_fig = go.Figure()
for val in equation_values:
    sp.plot(val, (x, -10, 10), show=False, line_color=np.random.choice(['blue', 'green', 'purple'])).show()
