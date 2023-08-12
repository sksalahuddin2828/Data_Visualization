import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Number of frames and matrix size
num_frames = 10
matrix_size = 5

# Generate a symmetric matrix sequence
frames = []
for i in range(num_frames):
    symmetric_matrix = np.random.randint(1, 10, size=(matrix_size, matrix_size))
    symmetric_matrix = (symmetric_matrix + symmetric_matrix.T) / 2  # Ensure symmetry
    frames.append(pd.DataFrame(symmetric_matrix))

# Create a subplot grid
fig = make_subplots(rows=1, cols=num_frames,
                    specs=[[{'type': 'surface'}] * num_frames],
                    subplot_titles=[f"Frame {i + 1}" for i in range(num_frames)])

# Add surfaces to subplots
for i, frame in enumerate(frames):
    x, y = np.meshgrid(np.arange(matrix_size), np.arange(matrix_size))
    fig.add_trace(
        go.Surface(x=x, y=y, z=frame.values, colorscale='Viridis'),
        row=1, col=i+1
    )

# Set layout for each subplot
for i in range(num_frames):
    fig.update_layout(scene=dict(aspectmode="data"),
                      scene_camera=dict(eye=dict(x=-1.5, y=-1.5, z=1)),
                      scene_xaxis_title="Columns",
                      scene_yaxis_title="Rows",
                      scene_zaxis_title="Values")

# Update layout
fig.update_layout(
    title="3D Evolution of Symmetric Matrix",
    width=1200,
    height=500,
    font=dict(size=10)
)

# Display the 3D animated subplot
fig.show()
