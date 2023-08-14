import plotly.graph_objects as go
import numpy as np

# Create data for the animation
num_frames = 100
theta_vals = np.linspace(0, 10 * np.pi, num_frames)
radii = np.linspace(0, 2, num_frames)
x_vals = radii * np.cos(theta_vals)
y_vals = radii * np.sin(theta_vals)

# Create the figure and initial trace
fig = go.Figure()
trace = go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=5, color='red'), showlegend=False)
fig.add_trace(trace)

# Define the animation frames
frames = [go.Frame(data=[go.Scatter(x=x_vals[:i+1], y=y_vals[:i+1], mode='markers', marker=dict(size=5, color='red'), showlegend=False)], name=str(i)) for i in range(1, num_frames)]

# Set up the animation settings
animation_settings = dict(frame=dict(duration=100, redraw=True), fromcurrent=True)
fig.frames = frames
fig.update(frames=frames, layout_updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play', method='animate', args=[None, animation_settings])])])

# Customize the layout
fig.update_layout(
    title='Animated Spiral Pattern with Tangent Function',
    xaxis=dict(title='X', showgrid=False),
    yaxis=dict(title='Y', showgrid=False),
    autosize=False,
    width=600,
    height=600
)

# Show the interactive plot
fig.show()
