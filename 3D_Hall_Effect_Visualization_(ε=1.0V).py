import numpy as np
import pandas as pd
import plotly.graph_objs as go

# Constants
B = 0.5  # Magnetic field strength (Tesla)
v = 2.0  # Velocity of charges (m/s)
l = 1.0  # Width of the conductor (m)

# Calculate Hall emf (ε)
epsilon = B * l * v

# Create a pandas DataFrame for charges' positions
num_charges = 100
charge_positions = np.linspace(0, l, num_charges)
charges_df = pd.DataFrame({'Position': charge_positions})

# Calculate the forces on charges due to the magnetic field
charges_df['Force'] = charges_df['Position'].apply(lambda x: -1 if x < l / 2 else 1) * v * B

# Create a 3D scatter plot to visualize charge movement
scatter_plot = go.Scatter3d(
    x=charges_df['Position'],
    y=np.zeros(num_charges),
    z=np.zeros(num_charges),
    mode='markers',
    marker=dict(
        size=5,
        color=charges_df['Force'],
        colorscale='Viridis',
        colorbar=dict(title='Force (N)'),
    ),
    text=charges_df['Force'],
)

# Create layout for the plot
layout = go.Layout(
    title=f'Hall Effect Visualization (ε = {epsilon} V)',
    scene=dict(
        xaxis_title='Position (m)',
        yaxis_title='',
        zaxis_title='',
    ),
)

# Create a figure and plot it using Plotly
fig = go.Figure(data=[scatter_plot], layout=layout)
fig.show()
