import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Constants
B = 0.2  # Magnetic field strength in Tesla
l = 1.0  # Length of wire in meters

# Generate random wire data
np.random.seed(0)
num_wires = 10
data = {
    'Current': np.random.uniform(1, 10, num_wires),  # Random currents between 1 and 10 A
    'Theta': np.random.uniform(0, 2 * np.pi, num_wires),  # Random angles
    'X': np.random.uniform(0, 5, num_wires),  # Random X coordinates
    'Y': np.random.uniform(0, 5, num_wires),  # Random Y coordinates
}

# Calculate magnetic forces
data['Fx'] = data['Current'] * l * B * np.sin(data['Theta']) * np.cos(data['Theta'])
data['Fy'] = data['Current'] * l * B * np.sin(data['Theta']) * np.sin(data['Theta'])

# Create a Pandas DataFrame
df = pd.DataFrame(data)

# Create a 3D Scatter plot using Plotly
fig = px.scatter_3d(df, x='X', y='Y', z='Theta', size='Current', color='Fx',
                     hover_data=['Current', 'Fx', 'Fy'], title='Magnetic Forces on Current-Carrying Wires')

# Customize the plot layout
fig.update_layout(scene=dict(aspectmode='manual', aspectratio=dict(x=1, y=1, z=0.3)))
fig.update_traces(marker=dict(showscale=True, colorbar=dict(title='Fx (N)')))

# Add axis labels
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Theta'))

# Show the interactive plot
fig.show()
