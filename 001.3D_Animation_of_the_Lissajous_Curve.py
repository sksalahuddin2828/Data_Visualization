import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Parameters for Lissajous curve
A = 1.0
B = 2.0
delta = np.pi / 2  # Phase difference

# Create a DataFrame to store Lissajous curve data
num_frames = 100
t_vals = np.linspace(0, 2 * np.pi, num_frames)
df = pd.DataFrame({'t': t_vals})

# Compute Lissajous curve coordinates
df['x'] = A * np.sin(3 * df['t'] + delta * np.cos(2 * df['t']))
df['y'] = B * np.sin(2 * df['t'])

# Create a subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter'}]])

# Add Lissajous curve trace
curve_trace = go.Scatter(
    x=df['x'],
    y=df['y'],
    mode='lines',
    line=dict(color='blue', width=2),
    name='Lissajous Curve'
)
fig.add_trace(curve_trace)

# Set layout
fig.update_layout(
    title='Interactive Lissajous Curve Animation',
    xaxis_title='X',
    yaxis_title='Y',
)

# Animation frame function
def update_trace(frame):
    frame_data = df.iloc[frame]
    fig.data[0].x = frame_data['x']
    fig.data[0].y = frame_data['y']

# Create animation frames
frames = [go.Frame(data=[go.Scatter(x=df['x'][:frame+1], y=df['y'][:frame+1])]) for frame in range(num_frames)]
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
