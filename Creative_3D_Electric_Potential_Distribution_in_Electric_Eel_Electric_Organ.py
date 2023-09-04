import pandas as pd
import numpy as np
import plotly.graph_objs as go

# Constants
voltage_per_cell = 0.15  # Voltage per electroplaques cell (V)
rows = 140
electroplaques_per_row = 5000

# Create a dataframe for electric organ information in Electric Eel
electric_organ_data = pd.DataFrame({
    'Row': np.repeat(np.arange(1, rows + 1), electroplaques_per_row),  # Row numbers
    'Electroplaques': np.tile(np.arange(1, electroplaques_per_row + 1), rows)  # Electroplaques per row
})

# Calculate electric potential at each electroplaques cell
electric_organ_data['Electric Potential (V)'] = voltage_per_cell * electric_organ_data['Electroplaques']

# Create a grid for 3D surface plot
x = electric_organ_data['Row'].values.reshape(electroplaques_per_row, rows)
y = electric_organ_data['Electroplaques'].values.reshape(electroplaques_per_row, rows)
z = electric_organ_data['Electric Potential (V)'].values.reshape(electroplaques_per_row, rows)

# Create a 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis')])

# Add theory and explanations as annotations
theory_annotation = dict(
    text="The electric potential distribution across the electric organ of an Electric Eel.",
    showarrow=False,
    x=20, y=3000,  # Adjust the position
    font=dict(size=10),
)
fig.add_annotation(theory_annotation)

# Customize the appearance of the plot
fig.update_layout(title='Electric Potential Distribution in Electric Eel Electric Organ',
                  scene=dict(xaxis_title='Rows', yaxis_title='Electroplaques', zaxis_title='Electric Potential (V)'),
                  scene_camera=dict(eye=dict(x=1.87, y=0.88, z=-0.64)))

# Show the interactive plot
fig.show()
