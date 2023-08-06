import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

def is_graph_planar(graph):
    return len(graph.edges()) <= 3 * len(graph.nodes()) - 6

def count_regions(graph):
    return len(list(nx.connected_components(graph)))

def draw_graph_2d(graph, title):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold')
    plt.title(title)
    plt.show()

def draw_graph_3d(graph, title):
    pos = nx.spring_layout(graph, dim=3, seed=42)
    edge_x = []
    edge_y = []
    edge_z = []

    for edge in graph.edges():
        x0, y0, z0 = pos[edge[0]]
        x1, y1, z1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        edge_z.extend([z0, z1, None])

    edge_trace = go.Scatter3d(
        x=edge_x, y=edge_y, z=edge_z,
        line=dict(width=1, color='grey'),
        mode='lines'
    )

    node_x = []
    node_y = []
    node_z = []
    for node in graph.nodes():
        x, y, z = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_z.append(z)

    node_trace = go.Scatter3d(
        x=node_x, y=node_y, z=node_z,
        mode='markers+text',
        marker=dict(size=8, line=dict(width=2), color='red'),
        text=[f'Node {node}' for node in graph.nodes()],
        textposition='bottom center'
    )

    fig = go.Figure(data=[edge_trace, node_trace])
    fig.update_layout(title=title, showlegend=False)
    fig.show()

# Example 1: Check if K5 is planar
K5 = nx.complete_graph(5)
print(f"Is K5 planar? {is_graph_planar(K5)}")
draw_graph_2d(K5, "K5 (2D Visualization)")
draw_graph_3d(K5, "K5 (3D Visualization)")

# Example 2: Check the number of regions in a graph
G = nx.Graph([(1, 2), (1, 3), (2, 3), (3, 4), (5, 4)])
print(f"Number of regions in the graph: {count_regions(G)}")
draw_graph_2d(G, "Graph G (2D Visualization)")
draw_graph_3d(G, "Graph G (3D Visualization)")
