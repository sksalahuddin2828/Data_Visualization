import networkx as nx
import plotly.graph_objects as go

def dijkstra_shortest_path(graph, source):
    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0

    visited = set()

    while len(visited) < len(graph.nodes()):
        # Find the nearest vertex
        min_distance = float('inf')
        nearest_vertex = None
        for node in graph.nodes():
            if distances[node] < min_distance and node not in visited:
                min_distance = distances[node]
                nearest_vertex = node

        visited.add(nearest_vertex)

        # Update distances through the nearest vertex
        for neighbor in graph[nearest_vertex]:
            new_distance = distances[nearest_vertex] + graph[nearest_vertex][neighbor]['weight']
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return distances

# Create the graph
G = nx.Graph()
edges = [('K', 'a', 4), ('K', 'b', 2), ('K', 'd', 15), ('a', 'c', 3), ('b', 'c', 7), ('c', 'd', 8), ('c', 'L', 25)]
G.add_weighted_edges_from(edges)

# Calculate the shortest paths from vertex K
shortest_paths_from_K = dijkstra_shortest_path(G, 'K')

# Output the results
print("Shortest Paths from K:")
print(shortest_paths_from_K)

# Function to get the path as a string
def get_shortest_path_string(paths, target):
    path = [target]
    while path[-1] in paths and isinstance(paths[path[-1]], str):
        path.append(paths[path[-1]])
    path.reverse()
    return ' -> '.join(path)

# Calculate the shortest path from K to L
shortest_path_K_to_L = get_shortest_path_string(shortest_paths_from_K, 'L')

# Output the shortest path from K to L
print("\nShortest Path from K to L:")
print(shortest_path_K_to_L)

# Create a visualization of the graph
pos = nx.spring_layout(G, seed=42)
edge_trace = go.Scatter(
    x=[],
    y=[],
    line=dict(width=0.5, color='grey'),
    hoverinfo='none',
    mode='lines'
)

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_trace['x'] += (x0, x1, None)
    edge_trace['y'] += (y0, y1, None)

node_trace = go.Scatter(
    x=[],
    y=[],
    text=[],
    mode='markers+text',
    textposition='bottom center',
    marker=dict(
        showscale=True,
        colorscale='Viridis',
        size=10,
        colorbar=dict(
            thickness=15,
            title='Node Connections',
            xanchor='left',
            titleside='right'
        )
    )
)

for node in G.nodes():
    x, y = pos[node]
    node_trace['x'] += (x,)
    node_trace['y'] += (y,)
    node_trace['text'] += (node,)

# Create a function to get edge labels for visualization
def get_edge_labels(G):
    edge_labels = {}
    for edge in G.edges():
        edge_labels[edge] = str(G[edge[0]][edge[1]]['weight'])
    return edge_labels

# Get edge labels for visualization
edge_labels = get_edge_labels(G)

# Create a visualization of the graph with edge labels
edge_trace_with_labels = go.Scatter(
    x=[],
    y=[],
    line=dict(width=0.5, color='grey'),
    hoverinfo='text',
    mode='lines+text',
    textposition='top center',
    textfont=dict(size=10),
    text=[],
)

for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_trace_with_labels['x'] += (x0, x1, None)
    edge_trace_with_labels['y'] += (y0, y1, None)
    edge_trace_with_labels['text'] += (edge_labels[edge],)

fig = go.Figure(data=[edge_trace_with_labels, node_trace],
                layout=go.Layout(
                    title='Graph Visualization with Edge Weights',
                    showlegend=False,
                    hovermode='closest',
                    margin=dict(b=0, l=0, r=0, t=0),
                    annotations=[dict(
                        ax=x0,
                        ay=y0,
                        axref='x',
                        ayref='y',
                        x=x1,
                        y=y1,
                        xref='x',
                        yref='y',
                        showarrow=True,
                        arrowhead=3,
                        arrowsize=2,
                        arrowwidth=1,
                    ) for x0, y0, x1, y1 in zip(edge_trace_with_labels['x'][:-1], edge_trace_with_labels['y'][:-1],
                                               edge_trace_with_labels['x'][1:], edge_trace_with_labels['y'][1:])]
                )
                )

# Add the shortest path from K to L as an annotation on the graph
for edge in shortest_path_K_to_L.split(' -> '):
    x, y = pos[edge]
    fig.add_annotation(
        go.layout.Annotation(
            x=x,
            y=y,
            xref='x',
            yref='y',
            text=edge,
            showarrow=True,
            font=dict(size=12),
            align='center',
            ax=0,
            ay=-40,
            bordercolor='black',
            borderwidth=2,
            borderpad=4,
            bgcolor='lightyellow',
            opacity=0.8,
        )
    )

fig.show()
