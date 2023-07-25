import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import networkx as nx
import plotly.graph_objects as go
from itertools import permutations

def is_hamiltonian_cycle(graph):
    n = len(graph)
    vertices = list(range(n))
    for perm in permutations(vertices):
        if graph[perm[-1]][perm[0]] == 1:  # Check if the last vertex is connected to the first vertex
            if all(graph[perm[i]][perm[i+1]] == 1 for i in range(n-1)):  # Check if other vertices are connected in the permutation
                return True
    return False

# Example graph represented as an adjacency matrix
graph_matrix = np.array([[0, 1, 1, 0],
                         [1, 0, 1, 1],
                         [1, 1, 0, 1],
                         [0, 1, 1, 0]])

# Create a NetworkX graph from the adjacency matrix
G = nx.Graph(graph_matrix)

# Create 3D coordinates for nodes using a layout algorithm
pos_3d = nx.spring_layout(G, dim=3, seed=42)

# Plot the graph in 3D
edge_x = []
edge_y = []
edge_z = []
for edge in G.edges():
    x0, y0, z0 = pos_3d[edge[0]]
    x1, y1, z1 = pos_3d[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_z.extend([z0, z1, None])

edge_trace = go.Scatter3d(x=edge_x, y=edge_y, z=edge_z, mode='lines', line=dict(color='rgb(44, 160, 44)', width=3))

node_x, node_y, node_z = zip(*list(pos_3d.values()))
node_trace = go.Scatter3d(x=node_x, y=node_y, z=node_z, mode='markers', marker=dict(size=10, color='rgb(255, 0, 0)'))

# Add labels to nodes
node_labels = list(G.nodes())
label_trace = go.Scatter3d(x=node_x, y=node_y, z=node_z, mode='text', text=node_labels, textposition='top center',
                           textfont=dict(size=12, color='rgb(0, 0, 0)'))

fig = go.Figure(data=[edge_trace, node_trace, label_trace])

# Set axis labels and title
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                  title='Creative 3D Visualization of Hamiltonian Cycle')

# Add a visually appealing background
fig.update_layout(scene=dict(bgcolor='rgba(240, 240, 240, 0.9)'))

fig.show()
