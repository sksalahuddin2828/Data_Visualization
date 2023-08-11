import networkx as nx
import plotly.graph_objects as go
import pandas as pd

# Create a graph using NetworkX
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6)])

# Find the maximum independent set using NetworkX
max_independent_set = nx.maximal_independent_set(G)

# Convert the graph to a Plotly figure
pos = nx.spring_layout(G)  # Layout for positioning nodes

edge_traces = []

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    color = "red" if edge[0] in max_independent_set and edge[1] in max_independent_set else "#888"
    edge_trace = go.Scatter(
        x=[x0, x1, None],
        y=[y0, y1, None],
        line=dict(width=0.5, color=color),
        hoverinfo="none",
        mode="lines",
    )
    edge_traces.append(edge_trace)

node_trace = go.Scatter(
    x=[],
    y=[],
    text=[],
    mode="markers",
    hoverinfo="text",
    marker=dict(
        showscale=True,
        colorscale="YlGnBu",
        size=10,
        colorbar=dict(tickvals=[], ticktext=[]),
    ),
)

for node in G.nodes():
    x, y = pos[node]
    node_trace["x"] += (x,)
    node_trace["y"] += (y,)

# Create the Plotly figure
fig = go.Figure(data=edge_traces + [node_trace])

# Update colorbar tickvals and ticktext
node_colors = [node for node in G.nodes() if node in max_independent_set]
node_trace["marker"]["colorbar"]["tickvals"] = node_colors
node_trace["marker"]["colorbar"]["ticktext"] = ["Red" if node in node_colors else "" for node in G.nodes()]

# Add nodes and edges to the figure

# Set layout for the Plotly figure
fig.update_layout(
    title="Maximal Independent Set Visualization",
    titlefont_size=16,
    showlegend=False,
    hovermode="closest",
    margin=dict(b=0, l=0, r=0, t=0),
)

# Show the Plotly figure
fig.show()
