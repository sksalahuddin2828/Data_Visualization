import numpy as np
import plotly.graph_objects as go

# Function to generate random cube orientations
def generate_random_orientations(count):
    return np.random.randint(0, 3, size=count)

# Function to generate random cube locations
def generate_random_locations(count):
    return np.random.permutation(np.arange(1, count + 1))

# Generate data for corner and edge cubies
corner_cubies = 8
edge_cubies = 12
total_cubies = corner_cubies + edge_cubies

corner_orientations = generate_random_orientations(corner_cubies)
corner_locations = generate_random_locations(corner_cubies)

edge_orientations = generate_random_orientations(edge_cubies)
edge_locations = generate_random_locations(edge_cubies)

# Create a 3D cube
cube = go.Mesh3d(
    x=[0, 1, 1, 0, 0, 1, 1, 0],
    y=[0, 0, 1, 1, 0, 0, 1, 1],
    z=[0, 0, 0, 0, 1, 1, 1, 1],
    i=[7, 0, 0, 3, 4, 4, 1, 2, 6, 5, 0, 4],
    j=[0, 4, 1, 2, 5, 6, 5, 1, 3, 2, 7, 7],
    k=[4, 5, 5, 6, 6, 7, 3, 3, 7, 6, 5, 3],
    opacity=0.5,
    color='lightgrey'
)

# Create scatter plots for corner and edge cubies
corner_trace = go.Scatter3d(
    x=corner_locations,
    y=corner_orientations,
    z=np.zeros(corner_cubies),
    mode='markers',
    marker=dict(size=6, color='red'),
    name='Corner Cubies'
)

edge_trace = go.Scatter3d(
    x=edge_locations,
    y=edge_orientations,
    z=np.ones(edge_cubies),
    mode='markers',
    marker=dict(size=6, color='blue'),
    name='Edge Cubies'
)

# Create the layout and add the cube and scatter plots
layout = go.Layout(
    scene=dict(
        xaxis=dict(title='Cubie Location'),
        yaxis=dict(title='Orientation'),
        zaxis=dict(title='Cubie Type'),
        aspectmode='cube'
    ),
    margin=dict(l=0, r=0, b=0, t=0),
    showlegend=True,
    legend=dict(x=0.05, y=0.95),
    title='Rubik\'s Cube Configurations'
)

# Create the figure and add the cube and scatter plots
fig = go.Figure(data=[cube, corner_trace, edge_trace], layout=layout)

# Show the interactive 3D plot
fig.show()
