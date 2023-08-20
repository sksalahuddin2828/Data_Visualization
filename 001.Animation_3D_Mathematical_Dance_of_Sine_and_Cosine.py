import numpy as np
import plotly.graph_objects as go
from sympy import symbols, sin, cos, lambdify
from plotly.subplots import make_subplots

# Create symbolic variables
x, a = symbols('x a')

# Define the expressions
expression = sin(a * x) * cos(a * x)
integrated_expression = -cos(2 * a * x) / (4 * a)

# Create a grid of 'a' and 'x' values
a_values = np.linspace(0.1, 2, 50)
x_values = np.linspace(0, 1, 50)
a_grid, x_grid = np.meshgrid(a_values, x_values)

# Define a function for NumPy evaluation
integrated_eval = lambdify((a, x), integrated_expression, "numpy")

# Evaluate the integrated expression for each 'a' and 'x' pair
integrated_results = np.empty_like(a_grid)
for i in range(a_values.shape[0]):
    for j in range(x_values.shape[0]):
        integrated_results[i, j] = integrated_eval(a_values[i], x_values[j])

# ... (previous code)

# Initialize subplots
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter3d'}, {'type': 'scatter3d'}]])

# Create an animated scatter plot of the original expression
original_data = [{'x': x_values, 'y': np.sin(a_val * x_values), 'z': np.cos(a_val * x_values)} for a_val in a_values]
original_scatter = go.Scatter3d(x=original_data[0]['x'], y=original_data[0]['y'], z=original_data[0]['z'], mode='lines')
fig.add_trace(original_scatter, row=1, col=1)

# Create an animated surface plot of the integrated result
integrated_surface = go.Surface(z=integrated_results, x=a_grid, y=x_grid)
fig.add_trace(integrated_surface, row=1, col=2)

# Define the frames for animation
frames = [go.Frame(data=[go.Scatter3d(x=original_data[i]['x'], y=original_data[i]['y'], z=original_data[i]['z'])],
                   name=str(a_val)) for i, a_val in enumerate(a_values)]

# Update layout for animation
fig.frames = frames
frame_animation_settings = dict(frame=dict(duration=100, redraw=True), fromcurrent=True)
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, frame_animation_settings])])])

# Set layout titles and labels
fig.update_layout(title='Mathematical Dance of Sine and Cosine', scene=dict(zaxis_title='Value'))
fig.update_layout(scene2=dict(xaxis_title='a', yaxis_title='x', zaxis_title='Integrated Result'))

# Show the figure
fig.show()
