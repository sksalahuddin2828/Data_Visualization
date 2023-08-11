import networkx as nx
import plotly.graph_objects as go
from IPython.display import display, clear_output
import time

# Create a graph using NetworkX
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6)])

# Convert the graph to a Plotly figure
pos = nx.spring_layout(G)  # Layout for positioning nodes

# Create an empty figure
fig = go.Figure()

for i, edge in enumerate(G.edges()):
    clear_output(wait=True)  # Clear the previous frame
    time.sleep(0.5)  # Pause for a short time
    
    edge_trace = go.Scatter(
        x=[pos[edge[0]][0], pos[edge[1]][0], None],
        y=[pos[edge[0]][1], pos[edge[1]][1], None],
        line=dict(width=0.5, color="#888"),
        hoverinfo="none",
        mode="lines",
    )

    fig.add_trace(edge_trace)
    
    # Add nodes and edges to the figure
    for node in G.nodes():
        x, y = pos[node]
        node_trace = go.Scatter(
            x=[x],
            y=[y],
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

        fig.add_trace(node_trace)
        
    # Update layout for the frame
    fig.update_layout(
        title=f"Maximal Independent Set - Step {i + 1}",
        titlefont_size=16,
        showlegend=False,
        hovermode="closest",
        margin=dict(b=0, l=0, r=0, t=0),
    )

    # Display the updated figure
    display(fig)

# Display the final frame
time.sleep(1)
clear_output(wait=True)
display(fig)
