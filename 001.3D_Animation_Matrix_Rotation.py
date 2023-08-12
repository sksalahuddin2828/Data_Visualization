import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from math import radians, cos, sin

# Generate initial matrix
initial_matrix = np.array([[4, 3], [2, 1]])

# Rotation function
def rotate_matrix(matrix, angle_deg):
    angle_rad = radians(angle_deg)
    rotation_matrix = np.array([[cos(angle_rad), -sin(angle_rad)], [sin(angle_rad), cos(angle_rad)]])
    rotated_matrix = np.dot(rotation_matrix, matrix)
    return rotated_matrix

# Generate rotated matrices for animation
num_frames = 20
rotated_matrices = [rotate_matrix(initial_matrix, i * (360 / num_frames)) for i in range(num_frames)]

# Convert matrices to pandas DataFrames
dfs = [pd.DataFrame(mat, columns=['Column 1', 'Column 2']) for mat in rotated_matrices]

# Create initial heatmap using plotly
fig = px.imshow(dfs[0], labels=dict(color="Matrix Transformation"), title="Matrix Rotation Animation")

# Mathematical expressions and annotations
expression_text = "Rotated Matrix = Rotation Matrix × Initial Matrix"
annotation = go.layout.Annotation(
    text=expression_text,
    showarrow=False,
    xref="paper",
    yref="paper",
    x=0.5,
    y=1,
    font=dict(size=14),
    bordercolor="black",
    borderwidth=1,
    bgcolor="white",
)

# Build animation
frames = [go.Frame(data=[go.Heatmap(z=df.values, colorscale='Viridis', showscale=False)], layout=go.Layout(annotations=[annotation])) for df in dfs]
fig.frames = frames

# Configure animation layout
fig.update_layout(
    updatemenus=[{
        'type': 'buttons',
        'x': 0.1,
        'y': 0,
        'xanchor': 'right',
        'yanchor': 'top',
        'buttons': [{
            'label': 'Play',
            'method': 'animate',
            'args': [None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}],
        }, {
            'label': 'Pause',
            'method': 'animate',
            'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
        }],
    }],
)

# Display the animation
fig.show()
