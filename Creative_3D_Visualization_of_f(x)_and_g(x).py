import numpy as np
import plotly.graph_objects as go
from scipy.optimize import root

# Define the functions f(x) and g(x)
def f(x):
    return 2 + np.sqrt(x + 1) + np.cbrt(1 - x)

def g(x):
    return np.log((np.log(1 - x) / np.log(1 + x)) ** 2) / np.log(1 - x ** 2)

# Generate x and y values
x_values = np.linspace(-0.99, 0.99, 100)

# Create a meshgrid for 3D plotting
X, Y = np.meshgrid(x_values, x_values)
Z_f = f(X)
Z_g = g(Y)

# Create the 3D plot using Plotly
fig = go.Figure()

# Plot f(x) as a surface
fig.add_trace(go.Surface(x=X, y=Y, z=Z_f, colorscale='viridis', opacity=0.7, name='f(x)'))

# Plot g(x) as a surface
fig.add_trace(go.Surface(x=X, y=Y, z=Z_g, colorscale='plasma', opacity=0.7, name='g(x)'))

# Function to solve the equation f(x) - g(y) = 0
def equation_to_solve(xy):
    x, y = xy
    return [f(x) - g(y), 0]  # The second element of the array is a dummy value (0).

# Find the intersection point (root) using scipy.optimize.root
result = root(equation_to_solve, [0, 0])
if result.success:
    root_x, root_y = result.x
    fig.add_trace(go.Scatter3d(x=[root_x], y=[root_y], z=[f(root_x)], mode='markers', marker=dict(size=8, color='red'), name='Root'))
else:
    print("Intersection point not found.")

# Set labels and title for the 3D plot
fig.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'),
                  title='Visualization of f(x) and g(x) in 3D')

# Show the plot
fig.show()
