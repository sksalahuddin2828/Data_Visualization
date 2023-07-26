import numpy as np
import plotly.graph_objects as go
from scipy.optimize import fsolve

# Define the functions f(x) and g(x)
def f(x):
    return 2 + np.sqrt(x + 1) + np.cbrt(1 - x)

def g(x):
    return np.log((np.log(1 - x) / np.log(1 + x)) ** 2) / np.log(1 - x ** 2)

# Additional functions
def h(x):
    return np.sin(x) + np.cos(x)

def k(x):
    return np.exp(x) + x**2

def m(x):
    return np.tanh(x)

# Generate x and y values
x_values = np.linspace(0.001, 0.99, 100)
y_values_f = f(x_values)
y_values_g = g(x_values)
y_values_h = h(x_values)
y_values_k = k(x_values)
y_values_m = m(x_values)

# Create a meshgrid for 3D plotting
X, Y = np.meshgrid(x_values, x_values)
Z_f = np.array([[f(x) for x in row] for row in X])
Z_g = np.array([[g(x) for x in row] for row in X])
Z_h = np.array([[h(x) for x in row] for row in X])
Z_k = np.array([[k(x) for x in row] for row in X])
Z_m = np.array([[m(x) for x in row] for row in X])

# Create 3D surface plots for each function
fig = go.Figure()

fig.add_trace(go.Surface(z=Z_f, x=X, y=Y, colorscale='viridis', name='f(x) = 2 + sqrt(x+1) + cbrt(1 - x)'))
fig.add_trace(go.Surface(z=Z_g, x=X, y=Y, colorscale='plasma', name='g(x) = log((log(1 - x) / log(1 + x))^2) / log(1 - x^2)'))
fig.add_trace(go.Surface(z=Z_h, x=X, y=Y, colorscale='magma', name='h(x) = sin(x) + cos(x)'))
fig.add_trace(go.Surface(z=Z_k, x=X, y=Y, colorscale='inferno', name='k(x) = exp(x) + x^2'))
fig.add_trace(go.Surface(z=Z_m, x=X, y=Y, colorscale='cividis', name='m(x) = tanh(x)'))

# Calculate the intersection point (root) of f(x) and g(x)
def equation_to_solve(x):
    return f(x) - g(x)

root = fsolve(equation_to_solve, 0.5)

# Create a 3D scatter plot for the root
fig.add_trace(go.Scatter3d(x=[root[0]], y=[root[0]], z=[f(root)], mode='markers', marker=dict(size=5, color='red'), name='Root (x={:.3f})'.format(root[0])))

# Update layout for title and axes labels
fig.update_layout(
    title='Visualization of Mathematical Functions in 3D',
    scene=dict(
        xaxis_title='x',
        yaxis_title='y',
        zaxis_title='z'
    ),
    scene_camera=dict(eye=dict(x=1.6, y=-1.6, z=0.8)),
    legend=dict(x=0, y=1, traceorder='normal')
)

# Show the plot
fig.show()
