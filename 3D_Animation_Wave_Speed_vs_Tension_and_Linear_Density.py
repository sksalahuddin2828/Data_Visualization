import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import sympy as sp

# Step 1: Deriving the Wave Speed Equation
v, FT, mu = sp.symbols('v FT mu')
wave_speed_equation = sp.sqrt(FT / mu)

# Step 2: Calculating Wave Speed
tension_value = 100.0
linear_density_value = 0.01
calculated_wave_speed = wave_speed_equation.subs([(FT, tension_value), (mu, linear_density_value)])
print("Calculated Wave Speed:", calculated_wave_speed)

# Step 3: Visualization
tension_range = np.linspace(1, 200, 100)
linear_density_range = np.linspace(0.01, 0.2, 100)

# Create meshgrid
T, LD = np.meshgrid(tension_range, linear_density_range)
wave_speed_values = np.sqrt(T / LD)

# Create 3D surface plot using Plotly
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'surface'}]])
surface = go.Surface(
    x=T, y=LD, z=wave_speed_values,
    colorscale='Viridis', colorbar_title='Wave Speed'
)
fig.add_trace(surface)

# Define play button
play_button = dict(
    x=0.1, y=0, xanchor='right', yanchor='middle',
    type='buttons',
    showactive=False,
    buttons=[
        dict(label='Play',
             method='animate',
             args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}]),
        dict(label='Pause',
             method='animate',
             args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}])
    ]
)
fig.update_layout(updatemenus=[play_button])

# Define animation frames
animation_frames = [go.Frame(data=[go.Surface(z=wave_speed_values[:i+1])]) for i in range(len(tension_range))]

# Add animation frames
fig.frames = animation_frames

# Update layout
fig.update_layout(
    title='Wave Speed vs Tension and Linear Density',
    scene=dict(
        xaxis_title='Tension (FT)',
        yaxis_title='Linear Density (mu)',
        zaxis_title='Wave Speed (v)'
    ),
    scene_aspectmode='data',
    scene_zaxis_type='log'  # Adjust the z-axis to log scale
)

# Show the animated plot
fig.show()
