import numpy as np
import plotly.graph_objs as go

# Define a mathematical function to visualize
def surface_function(x, y):
    return np.sin(np.sqrt(x**2 + y**2))

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = surface_function(X, Y)

# Create an interactive 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
fig.update_layout(title='Interactive 3D Surface Plot', scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
fig.show()
