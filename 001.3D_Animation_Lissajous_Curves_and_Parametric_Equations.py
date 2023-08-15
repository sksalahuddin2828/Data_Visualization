import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create a subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Define time values
t_vals = np.linspace(0, 2 * np.pi, 100)

# Parametric equations
x_parametric = 2 * np.cos(t_vals) + np.cos(2 * t_vals)
y_parametric = 2 * np.sin(t_vals) - np.sin(2 * t_vals)

# Lissajous curve parameters
A = 3
B = 2
delta = np.pi / 2

# Compute Lissajous curve coordinates
x_lissajous = A * np.sin(3 * t_vals + delta * np.cos(2 * t_vals))
y_lissajous = B * np.sin(2 * t_vals)

# Add parametric equation trace
parametric_trace = go.Scatter(
    x=x_parametric,
    y=y_parametric,
    mode='lines',
    name='Parametric Equation'
)

# Add Lissajous curve trace
lissajous_trace = go.Scatter(
    x=x_lissajous,
    y=y_lissajous,
    mode='lines',
    name='Lissajous Curve'
)

fig.add_trace(parametric_trace)
fig.add_trace(lissajous_trace)

# Set layout
fig.update_layout(
    title='Creative Animation: Lissajous Curves and Parametric Equations',
    xaxis_title='X',
    yaxis_title='Y',
)

# Animation frame function
def update_trace(frame):
    frame_data_parametric = {'x': x_parametric[:frame+1], 'y': y_parametric[:frame+1]}
    frame_data_lissajous = {'x': x_lissajous[:frame+1], 'y': y_lissajous[:frame+1]}
    with fig.batch_update():
        fig.data[0].x = frame_data_parametric['x']
        fig.data[0].y = frame_data_parametric['y']
        fig.data[1].x = frame_data_lissajous['x']
        fig.data[1].y = frame_data_lissajous['y']

# Create animation frames
num_frames = len(t_vals)
frames = [go.Frame(data=[
    go.Scatter(x=x_parametric[:frame+1], y=y_parametric[:frame+1]),
    go.Scatter(x=x_lissajous[:frame+1], y=y_lissajous[:frame+1])
]) for frame in range(num_frames)]
fig.frames = frames

# Add play and pause buttons
fig.update_layout(updatemenus=[dict(type="buttons", showactive=False,
                                      buttons=[dict(label="Play",
                                                     method="animate",
                                                     args=[None, {"frame": {"duration": 50, "redraw": True},
                                                                  "fromcurrent": True,
                                                                  "transition": {"duration": 0}}]),
                                               dict(label="Pause",
                                                    method="animate",
                                                    args=[[None], {"frame": {"duration": 0, "redraw": False},
                                                                  "mode": "immediate",
                                                                  "transition": {"duration": 0}}])])])

# Show the plot
fig.show()
