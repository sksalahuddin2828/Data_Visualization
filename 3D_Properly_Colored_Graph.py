import networkx as nx
import matplotlib.pyplot as plt

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
color_names = ['r', 'w', 'b', 'y', 'g', 'm', 'c', 'k']

# Assign colors to nodes
node_colors = [color_names[colors[node]] for node in G.nodes()]

# Draw the graph
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=500, font_size=12)

# Draw legend for colors
for i in range(num_colors):
    plt.scatter([], [], c=color_names[i], label=f"Color {i+1}")

# Show the legend
plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title="Colors", loc='lower right')

# Show the plot
plt.title("Properly Colored Graph")
plt.axis('off')
plt.show()
