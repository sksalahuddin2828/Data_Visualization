import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Generate sample data using Pandas
num_points = 50
currents = np.linspace(0, 5, num_points)
voltages = np.linspace(0, 120, num_points)
currents_mesh, voltages_mesh = np.meshgrid(currents, voltages)
powers = (1/2) * currents_mesh * voltages_mesh

data = pd.DataFrame({
    'Current': currents_mesh.flatten(),
    'Voltage': voltages_mesh.flatten(),
    'Power': powers.flatten()
})

# Create an interactive scatter plot using Plotly
scatter_plot = px.scatter_3d(data, x='Current', y='Voltage', z='Power', title='Average Power 3D Visualization')

# Create an interactive 3D surface plot using Plotly
surface_plot = go.Figure(data=[go.Surface(z=powers, x=currents, y=voltages)])
surface_plot.update_layout(title='Average Power 3D Surface Visualization')

# Display the plots
scatter_plot.show()
surface_plot.show()
