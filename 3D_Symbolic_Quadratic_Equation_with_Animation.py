import numpy as np
import pandas as pd
import sympy as sp
import plotly.graph_objs as go
from plotly.subplots import make_subplots

a_list = np.linspace(-10, 10, 100)
b_list = np.linspace(-10, 10, 100)
a_grid, b_grid = np.meshgrid(a_list, b_list)
c_grid = -a_grid - b_grid

# Create dataframe for quadratic roots and coefficients
roots_data = []
equation_data = []

for a_val, b_val, c_val in zip(a_list, b_list, c_list):
    roots = solve_quadratic(a_val, b_val, c_val)
    if roots is not None:
        roots_data.append({'a': a_val, 'b': b_val, 'c': c_val, 'roots': roots})
    
    x = sp.Symbol('x')
    equation = x**2 + b_val*x + c_val
    equation_data.append({'a': a_val, 'b': b_val, 'c': c_val, 'equation': equation})

df_roots = pd.DataFrame(roots_data)
df_equations = pd.DataFrame(equation_data)

# Create an animated scatter 3D plot
scatter_animation = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
scatter_animation.update_layout(scene=dict(xaxis_title='a', yaxis_title='b', zaxis_title='Roots'))

for i in range(len(df_roots)):
    roots = df_roots.loc[i, 'roots']
    if isinstance(roots, tuple):
        scatter_animation.add_trace(go.Scatter3d(
            x=[df_roots.loc[i, 'a']],
            y=[df_roots.loc[i, 'b']],
            z=[roots[0]],
            mode='markers',
            marker=dict(size=8, color='red', opacity=0.8),
            name='Real Roots'
        ))
        
scatter_animation.show()

# Create animated equations plot
equation_animation = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter', 'rowspan': 1}]])
equation_animation.update_layout(xaxis_title='x', yaxis_title='Equation Value')

for i in range(len(df_equations)):
    equation = df_equations.loc[i, 'equation']
    b_val = df_equations.loc[i, 'b']
    c_val = df_equations.loc[i, 'c']
    
    expression = equation.subs({sp.Symbol('b'): b_val, sp.Symbol('c'): c_val})
    
    # Convert symbolic expression to a lambda function for plotting
    func = sp.lambdify(sp.Symbol('x'), expression, "numpy")
    x_vals = np.linspace(-10, 10, 500)
    y_vals = func(x_vals)
    
    equation_animation.add_trace(go.Scatter(
        x=x_vals,
        y=y_vals,
        mode='lines',
        name=f'Equation for b={b_val}, c={c_val}'
    ))

equation_animation.show()
