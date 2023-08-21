import numpy as np
import pandas as pd
import plotly.graph_objects as go
from IPython.display import display, Markdown

def calculate_angular_displacement(omega_initial, alpha, time):
    return omega_initial * time + 0.5 * alpha * time ** 2

# Given values
rpm = 7000.0
t = 10.0
alpha_t = 73.3

# Calculate angular velocity (ω) and angular displacement (Δθ)
omega = rpm * (2 * np.pi) / 60
omega_initial = 0
delta_theta = omega ** 2 - omega_initial ** 2 / (2 * alpha_t)
delta_theta_calculated = calculate_angular_displacement(omega_initial, alpha_t, t)

markdown_text = '''
### Angular Velocity and Displacement

In this section, we'll explore the concepts of angular velocity and displacement.

**Angular Velocity (ω):** Angular velocity measures how fast an object is rotating. It's given by the formula:
$$
\\omega = \\frac{{\\text{{rpm}} \\times 2\\pi}}{{60}}
$$

**Angular Displacement (Δθ):** Angular displacement is the change in the angle of an object as it rotates. It can be calculated using the kinematic equation:
$$
\\Delta \\theta = \\omega_i \\times t + \\frac{1}{2} \\alpha \\times t^2
$$

Where:
- $$\\omega_i$$ is the initial angular velocity
- $$\\alpha$$ is the angular acceleration
- $$t$$ is the time
'''

# Display the Markdown text
display(Markdown(markdown_text))

# Create an interactive line plot using Plotly for angular velocity
time_values = np.linspace(0, t, 100)
angular_velocity_values = omega + alpha_t * time_values

fig_velocity = go.Figure()
fig_velocity.add_trace(go.Scatter(x=time_values, y=angular_velocity_values,
                                  mode='lines', name='Angular Velocity'))
fig_velocity.update_layout(title='Angular Velocity vs. Time',
                          xaxis_title='Time (s)', yaxis_title='Angular Velocity (rad/s)')

# Create an animated 3D surface plot using Plotly
theta_values = np.linspace(0, 2 * np.pi, 100)
time_values = np.linspace(0, t, 100)
theta, time = np.meshgrid(theta_values, time_values)
angular_velocity = omega + alpha_t * time

fig_surface = go.Figure()
fig_surface.add_trace(go.Surface(x=theta, y=time, z=angular_velocity,
                                 colorscale='viridis', colorbar_title='Angular Velocity'))
fig_surface.update_layout(scene=dict(xaxis_title='θ (rad)', yaxis_title='Time (s)',
                                     zaxis_title='Angular Velocity (rad/s)'),
                          title='3D Angular Velocity Visualization')
frames = [go.Frame(data=[go.Surface(x=theta, y=time, z=angular_velocity, colorscale='viridis')],
                   name=str(i)) for i in range(len(time_values))]
fig_surface.frames = frames

fig_velocity.show()
fig_surface.show()
