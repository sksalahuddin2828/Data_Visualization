import numpy as np
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots

# Sample 2x2 matrix
matrix = np.array([[3, 1], [2, 4]])

# Calculate determinant
det = np.linalg.det(matrix)

# Create Plotly figure
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'heatmap'}, {'type': 'scatter'}]])

# Plot the matrix heatmap
heatmap_trace = go.Heatmap(z=matrix, colorscale='Viridis')
fig.add_trace(heatmap_trace, row=1, col=1)

# Scatter plot for determinant
det_trace = go.Scatter(x=[0], y=[det], mode='markers', marker=dict(color='red', size=10))
fig.add_trace(det_trace, row=1, col=2)

# Update layout
fig.update_layout(title='2D Matrix Visualization',
                  xaxis_title='Column',
                  yaxis_title='Row',
                  yaxis=dict(scaleanchor="x", scaleratio=1),
                  xaxis2=dict(title='Determinant', showline=False, showticklabels=False),
                  showlegend=False)

# Show the interactive plot
fig.show()
