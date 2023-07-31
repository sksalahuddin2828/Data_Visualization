from sympy import Matrix

# Adjacency matrix of the graph
adjacency_matrix = np.zeros((num_vertices, num_vertices))
for edge in edges:
    u, v = edge
    adjacency_matrix[u - 1, v - 1] = 1
    adjacency_matrix[v - 1, u - 1] = 1

adjacency_matrix_sym = Matrix(adjacency_matrix)

# Convert the matrix to an edge list
edge_list = []
for i in range(num_vertices):
    for j in range(i + 1, num_vertices):
        if adjacency_matrix_sym[i, j] == 1:
            edge_list.append((i + 1, j + 1))

# Convert the edge list to a graph using NetworkX
import networkx as nx

G_sym = nx.Graph(edge_list)  # For undirected graph
# Or for directed graph:
# G_sym = nx.DiGraph(edge_list)

# Check if the graph is connected using NetworkX
is_connected_sym = nx.is_connected(G_sym)
print(f"Is the graph connected? {is_connected_sym}")

# Check if the graph is cyclic using NetworkX
is_cyclic_sym = nx.is_directed_acyclic_graph(G_sym)  # Only for directed graph
print(f"Is the graph cyclic? {not is_cyclic_sym}")

# Continue with the rest of the code for 3D visualization and additional statistics.
# Generate random z-coordinates for vertices in 3D plot
z_coordinates = np.random.rand(num_vertices)

# Create a 3D scatter plot using Plotly
fig_3d = go.Figure(data=[go.Scatter3d(
    x=vertices,
    y=df['Degree'],
    z=z_coordinates,
    text=df['Vertex'].astype(str),
    mode='markers',
    marker=dict(
        size=12,
        color=df['Degree'],
        colorscale='Viridis',
        opacity=0.8
    )
)])

# Set axis labels and title
fig_3d.update_layout(scene=dict(xaxis_title='Vertices', yaxis_title='Degree', zaxis_title='Z'),
                     title='Degrees of Vertices in Planar Graph (3D Visualization)')

# Show the 3D plot
fig_3d.show()

# Calculate average degree of vertices
average_degree = df['Degree'].mean()

# Calculate variance of degrees
degree_variance = df['Degree'].var()

# Print additional statistics
print(f"Average Degree: {average_degree}")
print(f"Degree Variance: {degree_variance}")

# Get vertices with highest and lowest degrees
vertex_max_degree = df.loc[df['Degree'].idxmax(), 'Vertex']
vertex_min_degree = df.loc[df['Degree'].idxmin(), 'Vertex']

print(f"Vertex with Highest Degree: {vertex_max_degree}")
print(f"Vertex with Lowest Degree: {vertex_min_degree}")
