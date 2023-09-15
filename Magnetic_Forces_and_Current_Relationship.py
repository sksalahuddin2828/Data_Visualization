import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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

# Create subplots for 3D scatter plot and 2D bar chart
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter3d'}, {'type': 'bar'}]])

# Create a 3D Scatter plot using Plotly
scatter = px.scatter_3d(df, x='X', y='Y', z='Theta', size='Current', color='Fx',
                         hover_data=['Current', 'Fx', 'Fy'],
                         title='Magnetic Forces on Current-Carrying Wires')

# Customize the 3D plot layout
scatter.update_layout(scene=dict(aspectmode='manual', aspectratio=dict(x=1, y=1, z=0.3)))
scatter.update_traces(marker=dict(showscale=True, colorbar=dict(title='Fx (N)')))

# Add axis labels to the 3D plot
scatter.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Theta'))

# Create a 2D Bar chart for additional information
bar_chart = px.bar(df, x='Current', y='Fx', title='Magnetic Force vs. Current')

# Add bar chart to the subplots
fig.add_trace(scatter.data[0], row=1, col=1)
fig.add_trace(bar_chart.data[0], row=1, col=2)

# Customize the bar chart layout
bar_chart.update_xaxes(title_text='Current (A)')
bar_chart.update_yaxes(title_text='Fx (N)')

# Update the overall layout
fig.update_layout(height=500, width=1000, title_text='Magnetic Forces and Current Relationship')

# Show the interactive plot
fig.show()
