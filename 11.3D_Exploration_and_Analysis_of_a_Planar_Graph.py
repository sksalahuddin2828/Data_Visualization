import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sympy import Matrix
import networkx as nx

# Generate random planar graph data
num_vertices = 10
num_edges = 20
vertices = np.arange(1, num_vertices + 1)
edges = [(np.random.randint(1, num_vertices + 1), np.random.randint(1, num_vertices + 1)) for _ in range(num_edges)]

# Calculate the degrees of regions and vertices
degrees = [0] * num_vertices
for edge in edges:
    degrees[edge[0] - 1] += 1
    degrees[edge[1] - 1] += 1

# Create a DataFrame to store the data
data = {'Vertex': vertices, 'Degree': degrees}
df = pd.DataFrame(data)

# Convert the edges into a NetworkX graph
G = nx.Graph()
G.add_edges_from(edges)

# Calculate the adjacency matrix of the graph
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
G_sym = nx.Graph(edge_list)

# Check if the graph is connected using NetworkX
is_connected_sym = nx.is_connected(G_sym)
print(f"Is the graph connected? {is_connected_sym}")

# Check if the graph is cyclic using NetworkX (only for directed graph)
is_cyclic_sym = nx.is_directed_acyclic_graph(G_sym)
print(f"Is the graph cyclic? {not is_cyclic_sym}")

# Calculate the shortest path lengths between all pairs of vertices
shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(G_sym))
path_lengths = [length for lengths in shortest_path_lengths.values() for length in lengths.values()]
average_path_length = sum(path_lengths) / len(path_lengths)
print(f"Average Path Length: {average_path_length:.2f}")

# Calculate the clustering coefficient for each vertex
clustering_coefficients = nx.clustering(G_sym)
df['Clustering Coefficient'] = df['Vertex'].map(clustering_coefficients)

# Calculate the PageRank values for each vertex
page_rank = nx.pagerank(G_sym)
df['PageRank'] = df['Vertex'].map(page_rank)

# Calculate the eccentricity of each vertex
eccentricity = nx.eccentricity(G_sym)
df['Eccentricity'] = df['Vertex'].map(eccentricity)

# Calculate the degree distribution
degree_distribution = df['Degree'].value_counts().sort_index()
degree_distribution_percentage = degree_distribution / len(df) * 100

# Visualize the degrees of vertices with Plotly
fig = go.Figure(data=[go.Bar(x=df['Vertex'], y=df['Degree'], marker=dict(color=df['Degree'], colorscale='viridis'))])
fig.update_layout(title='Degrees of Vertices in Planar Graph (Interactive)',
                  xaxis_title='Vertices', yaxis_title='Degree', template='plotly_dark')
fig.show()

# Visualize the clustering coefficient
plt.figure(figsize=(8, 6))
sns.barplot(x='Vertex', y='Clustering Coefficient', data=df, palette='viridis')
plt.xlabel('Vertices')
plt.ylabel('Clustering Coefficient')
plt.title('Clustering Coefficient of Vertices in Planar Graph')
plt.grid(axis='y')
plt.show()

# Visualize the PageRank values
plt.figure(figsize=(8, 6))
sns.barplot(x='Vertex', y='PageRank', data=df, palette='viridis')
plt.xlabel('Vertices')
plt.ylabel('PageRank Value')
plt.title('PageRank of Vertices in Planar Graph')
plt.grid(axis='y')
plt.show()

# Visualize the eccentricity
plt.figure(figsize=(8, 6))
sns.barplot(x='Vertex', y='Eccentricity', data=df, palette='viridis')
plt.xlabel('Vertices')
plt.ylabel('Eccentricity')
plt.title('Eccentricity of Vertices in Planar Graph')
plt.grid(axis='y')
plt.show()

# Visualize the degree distribution
plt.figure(figsize=(10, 6))
sns.barplot(x=degree_distribution.index, y=degree_distribution_percentage, palette='viridis')
plt.xlabel('Degree')
plt.ylabel('Percentage')
plt.title('Degree Distribution in Planar Graph')
plt.grid(axis='y')
plt.show()
