import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Parameters for Lissajous curve
A = 1.0
B = 2.0
delta = np.pi / 2  # Phase difference

# Create a DataFrame to store animation data
num_frames = 200
t_vals = np.linspace(0, 4 * np.pi, num_frames)
df = pd.DataFrame({'t': t_vals})

# Compute Lissajous curve coordinates
df['x_lissajous'] = A * np.sin(3 * df['t'] + delta * np.cos(2 * df['t']))
df['y_lissajous'] = B * np.sin(2 * df['t'])

# Create a spiral pattern
theta = np.linspace(0, 6 * np.pi, num_frames)
radius = 0.1 * t_vals
df['x_spiral'] = radius * np.cos(theta)
df['y_spiral'] = radius * np.sin(theta)

# Particle position along the Lissajous curve
df['x_particle'] = df['x_lissajous']
df['y_particle'] = df['y_lissajous']

# Create a subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Add Lissajous curve, spiral pattern, and particle traces
curve_trace = go.Scatter(
    x=df['x_lissajous'],
    y=df['y_lissajous'],
    mode='lines',
    line=dict(color='blue', width=2),
    name='Lissajous Curve'
)
spiral_trace = go.Scatter(
    x=df['x_spiral'],
    y=df['y_spiral'],
    mode='lines',
    line=dict(color='red', width=2),
    name='Spiral Pattern'
)
particle_trace = go.Scatter(
    x=[df['x_particle'][0]],
    y=[df['y_particle'][0]],
    mode='markers',
    marker=dict(size=10, color='green'),
    name='Particle'
)
fig.add_trace(curve_trace)
fig.add_trace(spiral_trace)
fig.add_trace(particle_trace)

# Set layout
fig.update_layout(
    title='Creative Math Visualization with Animation',
    xaxis_title='X',
    yaxis_title='Y',
)

# Animation frame function
def update_trace(frame):
    frame_data = df.iloc[frame]
    with fig.batch_update():
        fig.data[2].x = [frame_data['x_particle']]
        fig.data[2].y = [frame_data['y_particle']]

# Create animation frames
frames = [go.Frame(data=[
    go.Scatter(x=df['x_lissajous'][:frame+1], y=df['y_lissajous'][:frame+1]),
    go.Scatter(x=df['x_spiral'][:frame+1], y=df['y_spiral'][:frame+1]),
    go.Scatter(x=[df['x_particle'][frame]], y=[df['y_particle'][frame]], mode='markers', marker=dict(size=10, color='green')),
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
