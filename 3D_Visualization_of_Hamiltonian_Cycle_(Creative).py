import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import networkx as nx
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from itertools import permutations

# Example graph represented as an adjacency matrix
graph_matrix = np.array([[0, 1, 1, 0],
                         [1, 0, 1, 1],
                         [1, 1, 0, 1],
                         [0, 1, 1, 0]])

# Create a NetworkX graph from the adjacency matrix
G = nx.Graph(graph_matrix)

# Create 3D coordinates for nodes using a layout algorithm
pos_3d = nx.spring_layout(G, dim=3, seed=42)

# Define custom colors for nodes and edges
node_color = 'rgb(255, 140, 0)'
edge_color = 'rgb(0, 191, 255)'

# Create a 3D subplot
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]], subplot_titles=['Creative 3D Visualization of Hamiltonian Cycle'])

# Add edges to the subplot with a glowing effect
edge_x = []
edge_y = []
edge_z = []
for edge in G.edges():
    x0, y0, z0 = pos_3d[edge[0]]
    x1, y1, z1 = pos_3d[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_z.extend([z0, z1, None])

fig.add_trace(go.Scatter3d(x=edge_x, y=edge_y, z=edge_z, mode='lines', line=dict(color=edge_color, width=3),
                           hoverinfo='none', showlegend=False, opacity=0.8))

# Add nodes to the subplot
node_x, node_y, node_z = zip(*list(pos_3d.values()))
fig.add_trace(go.Scatter3d(x=node_x, y=node_y, z=node_z, mode='markers', marker=dict(size=12, color=node_color),
                           hoverinfo='none', showlegend=False))

# Add labels to nodes
node_labels = list(G.nodes())
fig.add_trace(go.Scatter3d(x=node_x, y=node_y, z=node_z, mode='text', text=node_labels, textposition='top center',
                           textfont=dict(size=8, color='rgb(255, 255, 255)'), hoverinfo='none', showlegend=False))

# Set axis labels and title
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                  width=800, height=600)

# Add a cosmic space background
fig.update_layout(scene=dict(bgcolor='rgb(0, 0, 0)'))

fig.show()
