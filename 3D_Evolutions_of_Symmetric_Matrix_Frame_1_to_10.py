import numpy as np
import plotly.graph_objects as go

# Number of frames and matrix size
num_frames = 10
matrix_size = 5

# Generate a symmetric matrix sequence
frames = []
for _ in range(num_frames):
    symmetric_matrix = np.random.randint(1, 10, size=(matrix_size, matrix_size))
    symmetric_matrix = (symmetric_matrix + symmetric_matrix.T) / 2  # Ensure symmetry
    frames.append(symmetric_matrix)

# Create the figure
fig = go.Figure()

# Create frames for the animation
for frame in frames:
    fig.add_trace(
        go.Surface(z=frame, colorscale='Viridis')
    )

# Set up slider steps
steps = []
for i in range(num_frames):
    step = dict(
        method="update",
        args=[{"visible": [False] * num_frames}],
    )
    step["args"][0]["visible"][i] = True
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "Frame: "},
    pad={"t": 50},
    steps=steps
)]

# Set layout
fig.update_layout(
    sliders=sliders,
    scene=dict(
        xaxis_title="Columns",
        yaxis_title="Rows",
        zaxis_title="Values",
        aspectmode="data",
        camera=dict(eye=dict(x=-1.5, y=-1.5, z=1))
    ),
    title="3D Evolution of Symmetric Matrix",
    width=1200,
    height=800,
    font=dict(size=10)
)

# Display the 3D animation
fig.show()
