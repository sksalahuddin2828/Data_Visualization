import networkx as nx
import itertools
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Create a sample graph
sauces = ['Tomato', 'Pesto', 'Alfredo', 'BBQ']
breads = ['Thin Crust', 'Regular', 'Whole Wheat', 'Gluten-Free']
cheeses = ['Mozzarella', 'Cheddar', 'Parmesan']

G = nx.Graph()
G.add_nodes_from(sauces, category='Sauce')
G.add_nodes_from(breads, category='Bread')
G.add_nodes_from(cheeses, category='Cheese')

for sauce, bread, cheese in itertools.product(sauces, breads, cheeses):
    G.add_edge(sauce, bread)
    G.add_edge(bread, cheese)

# 2D positions for nodes
pos = nx.spring_layout(G, seed=42)

# Create a 3D scatter plot
edge_trace = go.Scatter3d(
    x=[pos[edge[0]][0] for edge in G.edges()],
    y=[pos[edge[0]][1] for edge in G.edges()],
    z=[0] * len(G.edges()),  # Set z-coordinate to 0 for 2D visualization
    line=dict(color='blue', width=1),
    mode='lines'
)

node_trace = go.Scatter3d(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    z=[0] * len(G.nodes()),  # Set z-coordinate to 0 for 2D visualization
    text=list(G.nodes()),
    mode='markers+text',
    marker=dict(size=10, color='red')
)

fig_3d = go.Figure(data=[edge_trace, node_trace])

# Show the interactive 3D visualization
fig_3d.show()
