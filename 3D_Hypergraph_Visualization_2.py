import pandas as pd
import plotly.express as px

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

# Visualization using Plotly
edge_indices = []
vertex_labels = []

for idx, edge in enumerate(E):
    for vertex in edge:
        edge_indices.append(idx)
        vertex_labels.append(f"{vertex} ({V.index(vertex)})")

data = pd.DataFrame({
    'Edge': edge_indices,
    'VertexLabel': vertex_labels
})

fig = px.scatter(data, x='Edge', y=data.index, text='VertexLabel', title='Hypergraph Visualization',
                 labels={'Edge': 'Hyperedges'}, height=400)
fig.update_traces(textposition='top center')
fig.update_yaxes(visible=False, showticklabels=False)
fig.show()

# Checking if the hypergraph is k-regular
def is_k_regular(hypergraph, k):
    return all(len(edge) == k for edge in hypergraph)

k = 2  # Set k for k-regularity check
if is_k_regular(E, k):
    print(f"The hypergraph is {k}-regular.")
else:
    print(f"The hypergraph is not {k}-regular.")
