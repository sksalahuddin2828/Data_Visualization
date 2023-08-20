import sympy as sp

# Define symbolic variables
x, a = sp.symbols('x a')

# Define the expression and integrate
expression = a**2 + x**2
integral_result = sp.integrate(expression, x)
print("Integral Result:", integral_result)

# Answer: Integral Result: a**2*x + x**3/3

# Interactive Visualization with Plotly and ipywidgets

import numpy as np
import plotly.graph_objects as go
import ipywidgets as widgets
from IPython.display import display

# Define symbolic variables
x, a = sp.symbols('x a')

# Define the expression and integral result
expression = a**2 + x**2
integral_result = sp.atan(x / a)

# Initialize interactive sliders
a_slider = widgets.FloatSlider(value=1.0, min=0.1, max=2.0, step=0.1, description='a')
display(a_slider)

# Define x values for plotting
x_values = np.linspace(-5, 5, 400)

# Create a figure with Plotly for interactive visualization
fig = go.Figure()

# Define update function for slider
def update_figure(change):
    a_val = a_slider.value
    
    # Calculate expression and integral result
    expression_y = a_val**2 + x_values**2
    integral_y = np.arctan(x_values / a_val)
    
    # Update Plotly traces
    fig.data = []  # Clear previous traces
    fig.add_trace(go.Scatter(x=x_values, y=expression_y, name='Expression'))
    fig.add_trace(go.Scatter(x=x_values, y=integral_y, name='Integral Result'))
    
    # Update layout for Plotly figure
    fig.update_layout(title='Integration of (a^2 + x^2) dx = atan(x / a)', xaxis_title='x', yaxis_title='y')

# Connect slider to the update function
a_slider.observe(update_figure, names='value')

# Display the initial Plotly figure
fig.show()

# 3D Visualization with Matplotlib

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define a grid of 'a' and 'x' values
a_values = np.linspace(0.1, 2, 50)
x_values = np.linspace(-5, 5, 50)
a_grid, x_grid = np.meshgrid(a_values, x_values)

# Calculate the integral result for each pair of 'a' and 'x' values
integral_results = np.arctan(x_grid / a_grid)

# Create a 3D surface plot using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(a_grid, x_grid, integral_results, cmap='viridis')

# Set labels and title
ax.set_xlabel('a')
ax.set_ylabel('x')
ax.set_zlabel('Integral Result')
ax.set_title('3D Surface Plot of Integral Result')

# Show the plot
plt.show()
