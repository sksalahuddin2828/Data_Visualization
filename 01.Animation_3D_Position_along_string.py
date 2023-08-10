import numpy as np
import plotly.graph_objects as go

# Given values
linear_density_high_E = 3.09e-4  # kg/m
tension_high_E = 56.40  # N
length = 1.0  # Length of the string
time_points = 100
time_steps = 50

# Calculate wave speed using the formula: v = sqrt(FT / μ)
wave_speed_high_E = np.sqrt(tension_high_E / linear_density_high_E)

# Create a grid of points along the string
x = np.linspace(0, length, time_points)
t = np.linspace(0, 2 * np.pi, time_steps)
X, T = np.meshgrid(x, t)

# Calculate the wave motion using sine function
wave_high_E_3D = np.sin(2 * np.pi * X - wave_speed_high_E * T)

# Create the 3D surface plot
fig = go.Figure()

surf = go.Surface(x=X, y=T, z=wave_high_E_3D[:, 0], colorscale='Viridis')

fig.add_trace(surf)

# Update scene layout for 3D visualization
fig.update_layout(scene=dict(
    xaxis_title='Position along string',
    yaxis_title='Time',
    zaxis_title='Amplitude',
))

# Create animation frames
animation_frames = []

for i in range(time_steps):
    frame = go.Frame(data=[go.Surface(z=wave_high_E_3D[:, :i+1], colorscale='Viridis')])
    animation_frames.append(frame)

# Add frames to figure
fig.frames = animation_frames

# Set animation settings
animation_settings = [dict(label='Play', method='animate', args=[None, dict(frame=dict(duration=100, redraw=True), fromcurrent=True)])]

fig.update_layout(updatemenus=[dict(type='buttons', showactive=False, buttons=animation_settings)])

# Show interactive 3D plot
fig.show()
