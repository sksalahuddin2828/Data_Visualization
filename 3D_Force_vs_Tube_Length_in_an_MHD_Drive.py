import numpy as np
import pandas as pd
import plotly.express as px

# Constants
diameter_cm = 25.0
radius_m = diameter_cm / 100  # Convert to meters
current_A = 100
magnetic_field_T = 2.00

# Function to calculate force
def calculate_force(length_m):
    return current_A * magnetic_field_T * length_m

# Create a range of tube lengths
tube_lengths = np.linspace(0.01, 2.0, 100)  # Vary the length from 1 cm to 2 meters

# Calculate the corresponding forces
forces = [calculate_force(length) for length in tube_lengths]

# Create a Pandas DataFrame
data = pd.DataFrame({'Tube Length (m)': tube_lengths, 'Force (N)': forces})

# Create an interactive 3D surface plot using Plotly
fig = px.scatter_3d(data, x='Tube Length (m)', y='Force (N)', z=[0] * len(tube_lengths),
                    text='Tube Length (m)', title='Force vs. Tube Length in an MHD Drive',
                    labels={'Force (N)': 'Force (N)'}, template='plotly_dark')

# Customize the plot appearance
fig.update_traces(marker=dict(size=3), selector=dict(mode='markers+text'))
fig.update_layout(scene=dict(zaxis_title='', xaxis_title='Tube Length (m)', yaxis_title='Force (N)'))
fig.update_layout(scene_aspectmode='manual', scene_aspectratio=dict(x=1, y=1, z=0.1))
fig.update_layout(showlegend=False)

# Add a "mathematical dance" element
for i in range(0, len(tube_lengths), 10):
    fig.add_annotation(x=tube_lengths[i], y=forces[i], text=f'L={tube_lengths[i]:.2f}m',
                       font=dict(color='blue', size=10), showarrow=False, xshift=-10, yshift=10)

# Show the interactive plot
fig.show()
