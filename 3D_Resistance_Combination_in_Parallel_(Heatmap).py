import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Constants
R1_values = np.logspace(3, 6, 100)  # Vary R1 from 1kΩ to 1MΩ
R2_values = np.logspace(3, 6, 100)  # Vary R2 from 1kΩ to 1MΩ

# Calculate the equivalent resistance for all combinations
R_combination_values = 1 / (1 / R1_values[:, np.newaxis] + 1 / R2_values)

# Create a grid of R1 and R2 values
R1_grid, R2_grid = np.meshgrid(R1_values, R2_values)

# Create two separate figures for the 3D surface plot and heatmap
fig1 = go.Figure(go.Surface(x=np.log10(R1_grid), y=np.log10(R2_grid), z=np.log10(R_combination_values)))
fig2 = go.Figure(go.Heatmap(
    x=np.log10(R1_values),
    y=np.log10(R2_values),
    z=np.log10(R_combination_values),
    colorscale='Viridis',
    colorbar=dict(title='Log10(R_combination)'),
))

# Update layout for the 3D surface plot
fig1.update_layout(
    scene=dict(
        xaxis_title='Log10(R1)',
        yaxis_title='Log10(R2)',
        zaxis_title='Log10(R_combination)',
    ),
    title_text='Resistance Combination in Parallel (3D Surface Plot)'
)

# Update layout for the heatmap
fig2.update_layout(
    xaxis_title='Log10(R1)',
    yaxis_title='Log10(R2)',
    coloraxis_colorbar=dict(title='Log10(R_combination)'),
    title_text='Resistance Combination in Parallel (Heatmap)'
)

# Arrange the two figures side by side
fig1.update_layout(
    margin=dict(l=0, r=0, b=0, t=0),
    grid=dict(rows=1, columns=2),
    template='plotly',
)

# Create a subplot with the two figures
fig1.add_trace(go.Scatter(x=[None], y=[None], mode='markers', marker_opacity=0))  # Create an empty trace
fig1.add_trace(fig2.data[0])  # Add the heatmap trace to the subplot

# Show the combined plot
fig1.show()
