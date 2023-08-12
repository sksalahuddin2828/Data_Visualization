import numpy as np
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Number of frames and matrix size
num_frames = 10
matrix_size = 5

# Generate a symmetric matrix sequence
frames = []
for i in range(num_frames):
    symmetric_matrix = np.random.randint(1, 10, size=(matrix_size, matrix_size))
    symmetric_matrix = (symmetric_matrix + symmetric_matrix.T) / 2  # Ensure symmetry
    frames.append(pd.DataFrame(symmetric_matrix))

# Create subplots
fig = make_subplots(rows=1, cols=num_frames,
                    shared_yaxes=True,
                    subplot_titles=[f"Frame {i + 1}" for i in range(num_frames)])

# Add matrices as heatmaps to subplots
for i, frame in enumerate(frames):
    fig.add_trace(
        go.Heatmap(z=frame.values, colorscale='Viridis'),
        row=1, col=i+1
    )

# Set layout for each subplot
for i in range(num_frames):
    fig.update_xaxes(title_text="Columns", row=1, col=i+1)
    fig.update_yaxes(title_text="Rows", row=1, col=i+1)

# Update layout
fig.update_layout(
    title="Evolution of Symmetric Matrix",
    width=1000,
    height=400,
    font=dict(size=10)
)

# Display the animated subplot
fig.show()
