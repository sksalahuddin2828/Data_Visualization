import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Create an empty graph
G = nx.Graph()

# Add edges to the graph
edges = [(1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (6, 3)]
G.add_edges_from(edges)

# Get the proper coloring of the graph
colors = nx.coloring.greedy_color(G, strategy="largest_first")

# Number of colors used
num_colors = len(set(colors.values()))

# Create a list of color names for visualization
color_names = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan', 'black']

# Assign colors to nodes
node_colors = [color_names[colors[node]] for node in G.nodes()]

# Get positions of nodes using spring layout
pos = nx.spring_layout(G, seed=42)

# Create edges trace
edge_trace = go.Scatter(
    x=[pos[src][0] for src, dst in G.edges()] + [None],
    y=[pos[src][1] for src, dst in G.edges()] + [None],
    mode='lines',
    line=dict(width=0.5, color='grey'),
)

# Create nodes trace
node_trace = go.Scatter(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    mode='markers',
    marker=dict(
        showscale=True,
        colorscale='Viridis',
        size=10,
        colorbar=dict(
            thickness=15,
            title='Colors',
            xanchor='left',
            titleside='right'
        )
    )
)

# Set node colors in the nodes trace
node_trace.marker.color = node_colors

# Create the figure
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Properly Colored Graph',
                    titlefont_size=16,
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=0, l=0, r=0, t=40),
                    annotations=[dict(
                        text="",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002)],
                    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

# Show the plot
fig.show()
