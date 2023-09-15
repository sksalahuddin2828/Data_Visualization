import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given data
current = 30.0  # Amperes
force = 2.16  # Newtons
wire_length = 0.04  # meters (4.00 cm)

# Constants
mu_0 = 4 * np.pi * 1e-7  # Magnetic constant (permeability of free space)

# Create a grid of points in 3D space to represent the magnetic field
x = np.linspace(-0.1, 0.1, 20)
y = np.linspace(-0.1, 0.1, 20)
z = np.linspace(-0.02, 0.02, 20)
X, Y, Z = np.meshgrid(x, y, z)

# Calculate the magnetic field strength at each point due to the wire
def magnetic_field(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    B_x = (mu_0 * current * wire_length / (4 * np.pi)) * (x / r**3)
    B_y = (mu_0 * current * wire_length / (4 * np.pi)) * (y / r**3)
    B_z = (mu_0 * current * wire_length / (4 * np.pi)) * (z / r**3)
    return B_x, B_y, B_z

B_x, B_y, B_z = magnetic_field(X, Y, Z)

# Create a DataFrame for the magnetic field data
field_data = pd.DataFrame({'X': X.flatten(), 'Y': Y.flatten(), 'Z': Z.flatten(),
                            'B_x': B_x.flatten(), 'B_y': B_y.flatten(), 'B_z': B_z.flatten()})

# Create a 3D scatter plot of the magnetic field lines using Plotly
fig_3d = go.Figure(data=go.Scatter3d(
    x=field_data['X'],
    y=field_data['Y'],
    z=field_data['Z'],
    mode='markers',
    marker=dict(
        size=3,
        color=field_data['B_z'],  # Color based on B_z component
        colorscale='Viridis',
        colorbar=dict(title='Magnetic Field (B_z)'),
    )
))
fig_3d.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='Magnetic Field Lines Around a Wire',
)

# Create a mathematical expression to explain the magnetic field theory
expression = "B = μ₀ * I * L / (4π * r³)"

# Create an animated line plot of a magnetic field line
t = np.linspace(0, 2 * np.pi, 100)
r = 0.05  # Radial distance from the wire
x_line = r * np.cos(t)
y_line = r * np.sin(t)
z_line = np.linspace(-0.02, 0.02, 100)
B_x_line, B_y_line, B_z_line = magnetic_field(x_line, y_line, z_line)

# Create a sub-figure for the animated line plot
line_fig = go.Figure()
line_fig.add_trace(go.Scatter3d(
    x=x_line,
    y=y_line,
    z=z_line,
    mode='lines',
    line=dict(width=4, color='red'),
    name='Magnetic Field Line'
))

# Create an animation frame for the magnetic field line
frames = [go.Frame(data=[go.Scatter3d(
    x=x_line[:i],
    y=y_line[:i],
    z=z_line[:i],
    mode='lines',
    line=dict(width=4, color='red'),
    name='Magnetic Field Line'
)]) for i in range(2, len(x_line))]

line_fig.update(frames=frames)

# Display the interactive plots
fig_3d.show()
line_fig.show()

# Print the average field strength
average_field_strength = force / (current * wire_length)
print(f"Average Field Strength (B): {average_field_strength} Tesla")
