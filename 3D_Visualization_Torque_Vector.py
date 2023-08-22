import numpy as np
import plotly.graph_objects as go

# Given values
angle_deg = 80
r_perp = 98.5  # meters
force_magnitude = 5.0e5  # Newtons

# Calculate torque magnitude
torque_magnitude = -r_perp * force_magnitude

# Convert angle to radians
angle_rad = np.radians(angle_deg)

# Calculate torque vector components
torque_vector = np.array([
    torque_magnitude * np.sin(angle_rad),
    0,
    torque_magnitude * np.cos(angle_rad)
])

# Create an interactive 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=[0, torque_vector[0]],
    y=[0, torque_vector[1]],
    z=[0, torque_vector[2]],
    mode='markers+lines',
    marker=dict(size=[5, 0], color='blue'),
    line=dict(color='blue', width=5)
)])
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
        aspectmode='cube',
        camera=dict(eye=dict(x=1, y=1, z=1))
    )
)
fig.show()

import pandas as pd

data = {
    'Component': ['X', 'Y', 'Z'],
    'Value': torque_vector
}

torque_df = pd.DataFrame(data)
print(torque_df)
