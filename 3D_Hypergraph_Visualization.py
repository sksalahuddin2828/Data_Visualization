import matplotlib.pyplot as plt
import numpy as np

# Hypergraph representation
V = ['A', 'B', 'C', 'D', 'E']
E = [{V[0], V[3]}, {V[3], V[4]}, {V[0], V[1], V[2]}]

# Calculate order and size
def order(hypergraph):
    return len(hypergraph)

def size(hypergraph):
    return sum(len(edge) for edge in hypergraph)

hypergraph_order = order(E)
hypergraph_size = size(E)

print("Order of Hypergraph:", hypergraph_order)
print("Size of Hypergraph:", hypergraph_size)

# Visualization
for idx, edge in enumerate(E):
    x = np.ones(len(edge)) * idx
    y = np.arange(len(edge))
    plt.plot(x, y, 'o')

plt.xticks(np.arange(len(E)), ['e1', 'e2', 'e3'])
plt.yticks(np.arange(len(V)), V)
plt.xlabel('Hyperedges')
plt.ylabel('Vertices')
plt.title('Hypergraph Visualization')
plt.show()

# Checking if a hypergraph is empty
def is_empty(hypergraph):
    return len(hypergraph) == 0

if is_empty(E):
    print("The hypergraph is empty.")
else:
    print("The hypergraph is not empty.")
