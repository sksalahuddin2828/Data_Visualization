import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from scipy.optimize import fsolve

# Constants
emf_standard_cell = 12.0  # V
Rx_values = np.linspace(0.1, 10, 100)  # Array of Rx values
Rs_values = np.linspace(0.1, 10, 100)  # Array of Rs values

# Create a meshgrid of Rx and Rs values
Rx_mesh, Rs_mesh = np.meshgrid(Rx_values, Rs_values)

# Function to calculate EMF for given Rx and Rs
def calculate_emf(emf_cell, Rx, Rs):
    return emf_cell * Rs / (Rx + Rs) - emf_standard_cell

# Calculate EMF for each combination of Rx and Rs
emf_values = calculate_emf(emf_standard_cell, Rx_mesh, Rs_mesh)

# Create a DataFrame for visualization
df = pd.DataFrame({
    'Rx': Rx_mesh.flatten(),
    'Rs': Rs_mesh.flatten(),
    'EMF': emf_values.flatten()
})

# Create a 3D scatter plot
scatter_fig = px.scatter_3d(df, x='Rx', y='Rs', z='EMF', opacity=0.5,
                             title='EMF of the Cell vs. Rx and Rs')

# Create animation frames
frames = [go.Frame(
    data=[go.Surface(z=emf_values, x=Rx_mesh, y=Rs_mesh)],
    name=f'Frame_{emf:.1f}',
    layout=go.Layout(title=f'EMF of the Cell vs. Rx and Rs (EMF={emf:.1f} V)')
) for emf in np.linspace(0, 20, 50)]

# Add animation to the scatter plot
scatter_fig.update_traces(marker=dict(size=4), selector=dict(mode='markers'))
scatter_fig.update(frames=frames)

# Display the animation
scatter_fig.show()
