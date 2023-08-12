import numpy as np
import plotly.graph_objects as go

# Generate an orthogonal matrix
orthogonal_matrix = np.array([[np.cos(np.pi/4), -np.sin(np.pi/4)],
                              [np.sin(np.pi/4), np.cos(np.pi/4)]])

# Generate a set of unit vectors
num_points = 10
theta = np.linspace(0, 2 * np.pi, num_points)
unit_vectors = np.array([np.cos(theta), np.sin(theta)])

# Transform unit vectors using the orthogonal matrix
transformed_vectors = np.dot(orthogonal_matrix, unit_vectors)

# Create a scatter plot for original and transformed vectors
fig = go.Figure()

fig.add_trace(go.Scatter(x=unit_vectors[0], y=unit_vectors[1], mode='markers', name='Unit Vectors'))
fig.add_trace(go.Scatter(x=transformed_vectors[0], y=transformed_vectors[1], mode='markers', name='Transformed Vectors'))

# Add annotations to highlight properties of orthogonal matrices
fig.add_annotation(
    x=0, y=0,
    text="Preserves Length",
    arrowhead=2,
    showarrow=True
)
fig.add_annotation(
    x=orthogonal_matrix[0, 0], y=orthogonal_matrix[1, 0],
    text="Preserves Angles",
    arrowhead=2,
    showarrow=True
)
fig.add_annotation(
    x=orthogonal_matrix[0, 1], y=orthogonal_matrix[1, 1],
    text="Det(A) = ±1",
    arrowhead=2,
    showarrow=True
)

# Set layout options
fig.update_layout(
    title="Orthogonal Matrix Transformation",
    xaxis_title="X",
    yaxis_title="Y",
    legend=dict(x=0.7, y=0.9),
    annotations=[
        dict(
            xref="paper",
            yref="paper",
            x=0.95,
            y=0.1,
            showarrow=False,
            text="Note: Orthogonal matrices preserve lengths, angles, and have determinant ±1.",
        )
    ]
)

# Show the visualization
fig.show()
