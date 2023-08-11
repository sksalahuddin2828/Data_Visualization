import networkx as nx
import plotly.graph_objects as go
from IPython.display import display
import time

# Create a graph using NetworkX
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5), (4, 6)])

# Convert the graph to a Plotly figure
pos = nx.spring_layout(G)  # Layout for positioning nodes

# Create an empty figure
fig = go.Figure()

# Create frames for animation
frames = []
for i, edge in enumerate(G.edges()):
    edge_trace = go.Scatter(
        x=[pos[edge[0]][0], pos[edge[1]][0], None],
        y=[pos[edge[0]][1], pos[edge[1]][1], None],
        line=dict(width=0.5, color="#888"),
        hoverinfo="none",
        mode="lines",
    )

    node_trace = go.Scatter(
        x=[pos[node][0] for node in G.nodes()],
        y=[pos[node][1] for node in G.nodes()],
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

    # Create a frame for each step
    frame = go.Frame(data=[edge_trace, node_trace], name=f"Step {i + 1}")
    frames.append(frame)

    # Add the initial frame to the figure
    if i == 0:
        fig.add_trace(edge_trace)
        fig.add_trace(node_trace)

# Update layout for the initial frame
fig.update_layout(
    title="Maximal Independent Set - Step 1",
    titlefont_size=16,
    showlegend=False,
    hovermode="closest",
    margin=dict(b=0, l=0, r=0, t=0),
)

# Add frames to the figure
fig.frames = frames

# Add a play button
play_button = dict(
    type="buttons",
    x=0.1,
    y=0,
    xanchor="right",
    yanchor="top",
    showactive=False,
    buttons=[
        dict(
            label="Play",
            method="animate",
            args=[
                [f"Step {i + 1}" for i in range(len(frames))],
                {
                    "frame": {"duration": 500, "redraw": True},
                    "fromcurrent": True,
                    "transition": {"duration": 0},
                },
            ],
        )
    ],
)

fig.update_layout(updatemenus=[play_button])

# Display the figure
display(fig)
