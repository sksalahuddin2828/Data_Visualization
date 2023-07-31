import matplotlib.pyplot as plt

# Example planar graph data
vertices = [1, 2, 3, 4, 5]
edges = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 1)]

# Draw the graph
fig, ax = plt.subplots()
for edge in edges:
    x = [vertices[edge[0]-1], vertices[edge[1]-1]]
    y = [0, 0]  # Set y to 0 for simplicity
    ax.plot(x, y, marker='o', linestyle='-', color='b')

# Add region labels
regions = ['R1', 'R2', 'R3', 'R4']
for i, region in enumerate(regions):
    x = (vertices[i] + vertices[(i+1)%len(vertices)]) / 2
    y = 0
    ax.text(x, y, region, fontsize=12, ha='center', va='center')

ax.set_xticks(vertices)
ax.set_yticks([])
ax.set_xlabel('Vertices')
ax.set_title('Planar Graph with Regions')
plt.grid()
plt.show()
