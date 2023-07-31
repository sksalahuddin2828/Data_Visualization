import networkx as nx

# Convert the edges into a NetworkX graph
G = nx.Graph()
G.add_edges_from(edges)

# Calculate centrality measures
degree_centrality = nx.degree_centrality(G)
betweenness_centrality = nx.betweenness_centrality(G)
closeness_centrality = nx.closeness_centrality(G)

# Add centrality measures to the DataFrame
df['Degree Centrality'] = df['Vertex'].map(degree_centrality)
df['Betweenness Centrality'] = df['Vertex'].map(betweenness_centrality)
df['Closeness Centrality'] = df['Vertex'].map(closeness_centrality)

# Generate random edge weights
edge_weights = np.random.rand(num_edges)

# Add edge weights to the NetworkX graph
for i, (u, v) in enumerate(edges):
    G[u][v]['weight'] = edge_weights[i]

# Visualize the graph with edge weights
plt.figure(figsize=(10, 8))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12,
        width=[G[u][v]['weight'] * 4 for u, v in G.edges()], edge_color='grey', alpha=0.7, cmap=plt.cm.viridis)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=10)
plt.title('Random Planar Graph with Edge Weights')
plt.show()

