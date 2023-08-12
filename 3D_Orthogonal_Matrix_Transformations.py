import numpy as np
import plotly.graph_objects as go

# Create orthogonal matrix
orthogonal_matrix = np.array([[0.866, -0.5], [0.5, 0.866]])

# Create unit vectors
unit_vectors = np.array([[1, 0], [0, 1]])

# Transform unit vectors using the orthogonal matrix
transformed_vectors = np.dot(orthogonal_matrix, unit_vectors)

# Number of animation frames
num_frames = transformed_vectors.shape[1]

# Create a scatter plot for original and transformed vectors
fig = go.Figure()

# Add the original unit vectors
fig.add_trace(go.Scatter(x=unit_vectors[0], y=unit_vectors[1], mode='markers', name='Original Vectors'))

# Define the animation frames
frames = [go.Frame(data=[go.Scatter(x=transformed_vectors[0, :i+1], y=transformed_vectors[1, :i+1], mode='markers')]) for i in range(num_frames)]

# Add frames to the animation
for frame in frames:
    fig.add_trace(frame.data[0])

# Add animation settings
animation_settings = dict(
    frame=dict(duration=100, redraw=True),
    fromcurrent=True,
    transition=dict(duration=300, easing="quadratic-in-out")
)

# Add play and pause buttons to the animation
fig.update_layout(
    updatemenus=[
        dict(type="buttons", showactive=False, buttons=[
            dict(label="Play", method="animate", args=[None, animation_settings]),
            dict(label="Pause", method="animate", args=[[None], dict(frame=dict(duration=0, redraw=False), mode="immediate")])
        ])
    ]
)

# Set layout and show the animation
fig.update_layout(
    title="Orthogonal Matrix Transformation",
    xaxis=dict(range=[-1.5, 1.5]),
    yaxis=dict(range=[-1.5, 1.5]),
    xaxis_scaleanchor="y",
    yaxis_scaleanchor="x",
    showlegend=True
)

# Add animation frames to the layout
fig.frames = frames

# Show the animation
fig.show()
