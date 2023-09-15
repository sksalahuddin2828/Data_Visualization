import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given data
current = 30.0  # Amperes
force = 2.16  # Newtons
wire_length = 0.04  # meters (4.00 cm)

# Calculate the average field strength (B) using the formula: B = F / (I * L)
average_field_strength = force / (current * wire_length)

# Define a grid of points to represent the magnetic field
x = np.linspace(-0.1, 0.1, 20)
y = np.linspace(-0.1, 0.1, 20)
z = np.linspace(-0.02, 0.02, 20)
X, Y, Z = np.meshgrid(x, y, z)

# Calculate the magnetic field strength at each point due to the wire
mu_0 = 4 * np.pi * 1e-7  # Magnetic constant (permeability of free space)
B_x = (mu_0 * current * wire_length / (4 * np.pi)) * (X - 0) / ((X - 0)**2 + Y**2 + Z**2)**(3 / 2)
B_y = (mu_0 * current * wire_length / (4 * np.pi)) * Y / ((X - 0)**2 + Y**2 + Z**2)**(3 / 2)
B_z = (mu_0 * current * wire_length / (4 * np.pi)) * Z / ((X - 0)**2 + Y**2 + Z**2)**(3 / 2)

# Create a DataFrame for the magnetic field data
field_data = pd.DataFrame({'X': X.flatten(), 'Y': Y.flatten(), 'Z': Z.flatten(),
                            'B_x': B_x.flatten(), 'B_y': B_y.flatten(), 'B_z': B_z.flatten()})

# Create a 3D scatter plot of the magnetic field lines using Plotly
fig = go.Figure(data=go.Scatter3d(
    x=field_data['X'],
    y=field_data['Y'],
    z=field_data['Z'],
    mode='markers',
    marker=dict(
        size=2,
        color=field_data['B_z'],  # Color based on B_z component
        colorscale='Viridis',
        colorbar=dict(title='Magnetic Field (B_z)'),
    )
))

fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
    title='Magnetic Field Lines Around a Wire',
)

# Display the Plotly interactive plot
fig.show()

# Print the average field strength
print(f"Average Field Strength (B): {average_field_strength} Tesla")
