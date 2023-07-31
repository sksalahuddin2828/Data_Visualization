import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Visualize the degrees of vertices
plt.figure(figsize=(8, 6))
sns.barplot(x='Vertex', y='Degree', data=df, palette='viridis')
plt.xlabel('Vertices')
plt.ylabel('Degree')
plt.title('Degrees of Vertices in Planar Graph')
plt.grid(axis='y')
plt.show()
