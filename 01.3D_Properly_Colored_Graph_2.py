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

# Calculate the degrees of vertices
degrees = dict(G.degree())
node_size = [v * 100 for v in degrees.values()]

# Create edges trace
edge_trace = go.Scatter(
    x=[pos[src][0] for src, dst in G.edges()] + [None],
    y=[pos[src][1] for src, dst in G.edges()] + [None],
    mode='lines',
    line=dict(width=0.5, color='grey'),
    hoverinfo='none'
)

# Create nodes trace
node_trace = go.Scatter(
    x=[pos[node][0] for node in G.nodes()],
    y=[pos[node][1] for node in G.nodes()],
    mode='markers',
    marker=dict(
        showscale=True,
        colorscale='Viridis',
        size=node_size,
        colorbar=dict(
            thickness=15,
            title='Node Degree',
            xanchor='left',
            titleside='right'
        )
    ),
    text=[f'Degree: {degrees[node]}' for node in G.nodes()],
    hoverinfo='text'
)

# Set node colors in the nodes trace
node_trace.marker.color = node_colors

# Create the figure
fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Properly Colored Graph',
                    titlefont_size=20,
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

# Add labels for vertices
for node in G.nodes():
    x, y = pos[node]
    fig.add_annotation(
        x=x, y=y,
        text=f'Node {node}<br>Color: {node_colors[node - 1]}<br>Degree: {degrees[node]}',
        showarrow=True,
        arrowhead=1
    )

# Draw legend for colors
for i in range(num_colors):
    fig.add_trace(go.Scatter(
        x=[None],
        y=[None],
        mode='markers',
        marker=dict(
            showscale=False,
            size=10,
            color=color_names[i]
        ),
        showlegend=False
    ))

# Show the legend
fig.update_layout(legend_title_text='Colors', legend_traceorder='reversed')

# Show the plot
fig.show()
