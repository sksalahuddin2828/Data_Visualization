import numpy as np
import sympy as sp
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Define symbols
m, R, d = sp.symbols('m R d')

# Define equation
equation = sp.Eq(m * d**2, (13 * m * R**2))

# Solve the equation
solution = sp.solve(equation, d)

# Convert solution to a numerical function
R_value = 1.0  # Assign a value to R
solution_func = sp.lambdify(R, solution[0], 'numpy')
solution_value = solution_func(R_value)

# Define mass value
m_value = 2.0  # Assign an appropriate mass value

# Create a grid of points for visualization
grid_size = 30
x_vals = np.linspace(-R_value, R_value, grid_size)
y_vals = np.linspace(-R_value, R_value, grid_size)
x_grid, y_grid = np.meshgrid(x_vals, y_vals)
z_grid = np.zeros_like(x_grid)

# Calculate the moment of inertia for each position
inertia_values = [m_value * r**2 for r in x_vals]

# Create a list of DataFrames for animation frames
frames_data = []
for frame_num in range(grid_size):
    frame = pd.DataFrame({
        'x': [0, solution_value],
        'y': [0, 0],
        'z': [0, 0]
    })
    frame['x_obj'] = x_vals[frame_num]
    frame['moment_of_inertia'] = inertia_values[frame_num]
    frames_data.append(frame)

# Create the animated scatter plot using Plotly Express
fig = px.scatter_3d(
    frames_data[0],
    x='x',
    y='y',
    z='z',
    text=["Center of Mass", "Object Position"],
    custom_data=['moment_of_inertia'],
    labels={'x': 'X-axis', 'y': 'Y-axis', 'z': 'Z-axis'},
    animation_frame='x_obj',
    title="Animated 3D Visualization of Moment of Inertia Problem",
)

# Add a surface representing the object's position
fig.add_surface(
    x=x_grid,
    y=y_grid,
    z=z_grid,
    colorscale='Viridis',
    showscale=False,
    opacity=0.7
)

# Add annotations for dynamic information
annotation_template = "<b>Moment of Inertia</b>: %{customdata:.2f}<br>%{text}"
fig.update_traces(hovertemplate=annotation_template, selector=dict(mode='markers'))

# Customize the scene to add a line connecting the points
fig.update_layout(
    scene=dict(
        aspectmode="cube",
        camera=dict(eye=dict(x=-1, y=-1, z=1.5)),
    ),
    updatemenus=[
        {
            'buttons': [
                {
                    'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}],
                    'label': 'Play',
                    'method': 'animate',
                },
                {
                    'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                    'label': 'Pause',
                    'method': 'animate',
                },
            ],
            'direction': 'left',
            'pad': {'r': 10, 't': 87},
            'showactive': False,
            'type': 'buttons',
            'x': 0.1,
            'xanchor': 'right',
            'y': 0,
            'yanchor': 'top',
        },
    ],
    sliders=[
        {
            'active': 0,
            'yanchor': 'top',
            'xanchor': 'left',
            'currentvalue': {
                'font': {'size': 20},
                'prefix': 'Object Position:',
                'visible': True,
                'xanchor': 'right',
            },
            'transition': {'duration': 300, 'easing': 'cubic-in-out'},
            'pad': {'b': 10, 't': 50},
            'len': 0.9,
            'x': 0.1,
            'y': 0,
        },
    ],
)

# Add dynamic line connecting the points
dynamic_line = go.Scatter3d(
    x=[0, frames_data[0]['x_obj'][1]],
    y=[0, 0],
    z=[0, 0],
    line=dict(color="red", width=4),
    hoverinfo="none",
    customdata=[frames_data[0]['moment_of_inertia'][1]],
    hovertemplate="<b>Moment of Inertia</b>: %{customdata:.2f}",
    mode='lines'
)
fig.add_trace(dynamic_line)

# Add moment of inertia indicator
moment_of_inertia_indicator = go.Scatter3d(
    x=[frames_data[0]['x_obj'][1]],
    y=[0],
    z=[0],
    mode='markers',
    marker=dict(size=10, color="red"),
    customdata=[frames_data[0]['moment_of_inertia'][1]],
    hovertemplate="<b>Moment of Inertia</b>: %{customdata:.2f}",
    hoverinfo="skip"
)
fig.add_trace(moment_of_inertia_indicator)

# Update the dynamic line and moment of inertia indicator in each frame
def update_dynamic_line(frame_num):
    dynamic_line.x = [0, frames_data[frame_num]['x_obj'][1]]
    dynamic_line.y = [0, 0]
    dynamic_line.z = [0, 0]
    dynamic_line.customdata = [frames_data[frame_num]['moment_of_inertia'][1]]

    moment_of_inertia_indicator.x = [frames_data[frame_num]['x_obj'][1]]
    moment_of_inertia_indicator.y = [0]
    moment_of_inertia_indicator.z = [0]
    moment_of_inertia_indicator.customdata = [frames_data[frame_num]['moment_of_inertia'][1]]

# Create frames for the animation
frames = [go.Frame(data=[go.Scatter3d(x=[0, frames_data[frame_num]['x_obj'][1]],
                                      y=[0, 0],
                                      z=[0, 0],
                                      mode='lines',
                                      line=dict(color="red", width=4),
                                      customdata=[frames_data[frame_num]['moment_of_inertia'][1]],
                                      hovertemplate="<b>Moment of Inertia</b>: %{customdata:.2f}",
                                      hoverinfo="none"),
                      go.Scatter3d(x=[frames_data[frame_num]['x_obj'][1]],
                                   y=[0],
                                   z=[0],
                                   mode='markers',
                                   marker=dict(size=10, color="red"),
                                   customdata=[frames_data[frame_num]['moment_of_inertia'][1]],
                                   hovertemplate="<b>Moment of Inertia</b>: %{customdata:.2f}",
                                   hoverinfo="skip")
                      ]) for frame_num in range(grid_size)]

# Assign frames to the animation configuration
fig.frames = frames

# Show the interactive animated plot
fig.show()
