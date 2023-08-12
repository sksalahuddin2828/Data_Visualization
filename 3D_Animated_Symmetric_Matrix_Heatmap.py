import numpy as np
import pandas as pd
import plotly.express as px

# Number of frames and matrix size
num_frames = 10
matrix_size = 5

# Generate a list of symmetric matrices for animation
frames = []
for i in range(num_frames):
    symmetric_matrix = np.random.randint(1, 10, size=(matrix_size, matrix_size))
    symmetric_matrix = (symmetric_matrix + symmetric_matrix.T) / 2  # Ensure symmetry
    frames.append(pd.DataFrame(symmetric_matrix))

# Create an animated heatmap using plotly
fig = px.imshow(frames[0],
                zmin=0, zmax=10,
                color_continuous_scale='Viridis',
                title="Animated Symmetric Matrix Heatmap")

# Add frames to the animation
for frame in frames[1:]:
    fig.add_trace(px.imshow(frame,
                            zmin=0, zmax=10,
                            color_continuous_scale='Viridis').data[0])

# Update animation layout
fig.update_layout(
    xaxis_title="Columns",
    yaxis_title="Rows",
    xaxis_nticks=matrix_size,
    yaxis_nticks=matrix_size,
    xaxis_side="top",
    width=500,
    height=500,
    font=dict(size=10)
)

# Define animation settings
animation_settings = dict(frame=dict(duration=500, redraw=True), fromcurrent=True)

# Add animation controls
fig.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                buttons=[dict(label='Play',
                                              method='animate',
                                              args=[None, animation_settings])])])

# Add frames to animation
frame_annotations = [dict(text=f'Frame {i + 1}', showarrow=False,
                          xanchor='left', x=0.05, yanchor='top', y=0.95) for i in range(num_frames)]
fig.update_layout(annotations=frame_annotations)

# Display the animated heatmap
fig.show()
