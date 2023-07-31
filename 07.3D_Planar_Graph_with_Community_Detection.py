# Detect communities using the Louvain algorithm
from community import community_louvain

partition = community_louvain.best_partition(G)

# Add community information to the DataFrame
df['Community'] = df['Vertex'].map(partition)

# Visualize the graph with community colors
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=3000, font_size=12,
        node_color=list(partition.values()), cmap='tab20', alpha=0.8)
plt.title('Planar Graph with Community Detection')
plt.show()
