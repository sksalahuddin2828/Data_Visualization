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

# Check if the graph is connected
is_connected = nx.is_connected(G)
print(f"Is the graph connected? {is_connected}")

# Highlight connected components if the graph is not connected
if not is_connected:
    components = list(nx.connected_components(G))
    component_colors = [i for i in range(len(components)) for _ in components[i]]
    
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_size=3000, font_size=12,
            node_color=component_colors, cmap='tab20', alpha=0.8)
    plt.title('Planar Graph with Highlighted Connected Components')
    plt.show()
