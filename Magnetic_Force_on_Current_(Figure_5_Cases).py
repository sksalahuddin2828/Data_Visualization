import numpy as np
import pandas as pd
import plotly.express as px

# Define the magnetic field vector (B) and current vector (I) for each case
data = {
    'Case': ['a', 'b', 'c', 'd', 'e', 'f'],
    'B_x': [0, 1, 0, 1, 0, -1],
    'B_y': [0, 0, 1, 0, -1, 0],
    'B_z': [-1, 0, 0, 0, 0, 0],
    'I_x': [0, 0, 1, -1, 0, 0],
    'I_y': [0, -1, 0, 0, 0, 0],
    'I_z': [-1, 0, 0, 0, 1, 0]
}

df = pd.DataFrame(data)

# Calculate the magnetic force vector (F) for each case
df['F_x'] = df['I_y'] * df['B_z'] - df['I_z'] * df['B_y']
df['F_y'] = df['I_z'] * df['B_x'] - df['I_x'] * df['B_z']
df['F_z'] = df['I_x'] * df['B_y'] - df['I_y'] * df['B_x']

# Create an interactive 3D scatter plot
fig = px.scatter_3d(df, x='F_x', y='F_y', z='F_z', color='Case',
                     labels={'F_x': 'F_x', 'F_y': 'F_y', 'F_z': 'F_z'},
                     title='Magnetic Force on Current (Figure 5 Cases)')

# Customize the layout
fig.update_layout(scene=dict(aspectmode="cube"))
fig.update_traces(marker=dict(size=5))

# Show the interactive plot
fig.show()
