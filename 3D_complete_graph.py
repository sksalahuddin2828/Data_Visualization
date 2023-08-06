# pip install numpy matplotlib networkx

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

def is_graph_planar(graph):
    return len(graph.edges()) <= 3 * len(graph.nodes()) - 6

def draw_graph(graph, title):
    pos = nx.spring_layout(graph, seed=42)
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=10, font_weight='bold')
    plt.title(title)
    plt.show()

# Example 1: Check if K5 is non-planar
K5 = nx.complete_graph(5)
print(f"Is K5 non-planar? {not is_graph_planar(K5)}")
draw_graph(K5, "K5")

# Example 2: Check if the given graphs are non-planar
G1 = nx.Graph([(1, 2), (1, 3), (2, 3), (3, 4), (5, 4)])
G2 = nx.Graph([(1, 2), (1, 3), (1, 4), (5, 2), (5, 3), (5, 4)])

print(f"Is G1 non-planar? {not is_graph_planar(G1)}")
draw_graph(G1, "Graph G1")

print(f"Is G2 non-planar? {not is_graph_planar(G2)}")
draw_graph(G2, "Graph G2")
