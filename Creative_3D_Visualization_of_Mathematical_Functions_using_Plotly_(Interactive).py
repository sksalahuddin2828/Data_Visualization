import numpy as np
import plotly.graph_objects as go

# Define the functions f(x) and g(x)
def f(x):
    return 2 + np.sqrt(x + 1) + np.cbrt(1 - x)

def g(x):
    return np.log((np.log(1 - x) / np.log(1 + x)) ** 2) / np.log(1 - x ** 2)

# Generate x and y values
x_values = np.linspace(-0.99, 0.99, 100)
y_values_f = f(x_values)
y_values_g = g(x_values)

# Create a meshgrid for 3D plotting
X, Y = np.meshgrid(x_values, x_values)
Z_f = np.array([[f(x) for x in row] for row in X])
Z_g = np.array([[g(x) for x in row] for row in X])

# Create the 3D plot for f(x)
fig_f = go.Figure(data=[go.Surface(z=Z_f, x=X, y=Y, colorscale='viridis')])
fig_f.update_layout(title='f(x) = 2 + sqrt(x+1) + cbrt(1 - x)', scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'))

# Create the 3D plot for g(x)
fig_g = go.Figure(data=[go.Surface(z=Z_g, x=X, y=Y, colorscale='plasma')])
fig_g.update_layout(title='g(x) = log((log(1 - x) / log(1 + x))^2) / log(1 - x^2)', scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'))

# Calculate the intersection point (root) of the two surfaces
from scipy.optimize import fsolve

def equation_to_solve(x):
    return f(x) - g(x)

root = fsolve(equation_to_solve, 0)

# Create a 3D scatter plot for the root
fig_scatter = go.Figure(data=[go.Scatter3d(x=[root[0]], y=[root[0]], z=[f(root)], mode='markers', marker=dict(size=5, color='red'))])

# Combine the two plots
fig_combined = go.Figure(data=[fig_f.data[0], fig_g.data[0], fig_scatter.data[0]])
fig_combined.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'), title='Visualization of f(x) and g(x) in 3D')

# Show the combined plot
fig_combined.show()
