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

# Update the graph by adding vertex 'a' to S and calculate the new shortest paths
shortest_paths_from_K_and_a = dijkstra_shortest_path(G, 'a')

# Output the updated results
print("\nShortest Paths from K and a:")
print(shortest_paths_from_K_and_a)

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

fig = go.Figure(data=[edge_trace, node_trace],
                layout=go.Layout(
                    title='Graph Visualization',
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
                        yref='y'
                    ) for x0, y0, x1, y1 in zip(edge_trace['x'][:-1], edge_trace['y'][:-1],
                                               edge_trace['x'][1:], edge_trace['y'][1:])]
                )
                )
fig.show()
