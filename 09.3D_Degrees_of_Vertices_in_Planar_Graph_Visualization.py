from mpl_toolkits.mplot3d import Axes3D

# Generate random z-coordinates for vertices
z_coordinates = np.random.rand(num_vertices)

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot vertices in 3D
ax.scatter(vertices, df['Degree'], z_coordinates, c=df['Degree'], cmap='viridis', s=100)

# Add labels to the vertices
for (x, y, z, label) in zip(vertices, df['Degree'], z_coordinates, df['Vertex']):
    ax.text(x, y, z, str(label), fontsize=12, ha='center')

# Set axis labels
ax.set_xlabel('Vertices')
ax.set_ylabel('Degree')
ax.set_zlabel('Z')

# Set title
plt.title('Degrees of Vertices in Planar Graph (3D Visualization)')

# Show the 3D plot
plt.show()
