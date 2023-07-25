import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import sympy as sp

# Mathematical Dance and Expressions
x, y = sp.symbols('x y')
equation1 = sp.log(y, x) + sp.log(x, y) - 10
equation2 = sp.log(2*y, x) + sp.log(2*x, y) - 20
solutions = sp.solve((equation1, equation2), (x, y))

if len(solutions) > 0:
    x_val, y_val = solutions[0]
    print(f"The values of x and y are: {x_val}, {y_val}")
else:
    print("No solution found.")

# Prepare the data for 3D plot
x_vals = np.linspace(1, 10, 100)
y_vals = np.linspace(1, 10, 100)
x_grid, y_grid = np.meshgrid(x_vals, y_vals)

log_equation1 = np.log(y_grid) / np.log(x_grid) + np.log(x_grid) / np.log(y_grid) - 10
log_equation2 = np.log(2 * y_grid) / np.log(x_grid) + np.log(2 * x_grid) / np.log(y_grid) - 20

# Create the 3D plot
fig = go.Figure(data=[
    go.Surface(z=log_equation1, x=x_vals, y=y_vals, colorscale='Viridis', name='log(y) + log(x) = 10'),
    go.Surface(z=log_equation2, x=x_vals, y=y_vals, colorscale='Blues', opacity=0.8, name='log(2y) + log(2x) = 20')
])

fig.update_layout(
    title='3D Visualization of Logarithmic Equations',
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='log equation value',
    ),
    width = 1280,  # Adjust the width and height as per your preference
    height = 800,
)

fig.show()
