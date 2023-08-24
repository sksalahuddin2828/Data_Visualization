import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
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

# Mathematical expressions and animation
t = np.linspace(0, 2 * np.pi, 100)
x = np.cos(t)
y = np.sin(t)

expressions = {
    'x': 'cos(t)',
    'y': 'sin(t)'
}

eq = f"x = {expressions['x']}, y = {expressions['y']}"

fig = go.Figure(data=go.Scatter(x=x, y=y, mode='markers'))
fig.add_trace(go.Scatter(x=[x[0]], y=[y[0]], mode='markers+text', text=[f't = {t[0]:.2f}'], textposition="top right"))
fig.add_trace(go.Scatter(x=[x[-1]], y=[y[-1]], mode='markers+text', text=[f't = {t[-1]:.2f}'], textposition="bottom left"))
fig.update_layout(title="Parametric Circle Animation", xaxis_title="x", yaxis_title="y",
                  annotations=[dict(text=eq, x=0.5, y=1.1, showarrow=False)])
frames = [go.Frame(data=[go.Scatter(x=x[:i+1], y=y[:i+1], mode='markers+lines')]) for i in range(len(x))]
fig.frames = frames

fig.update_layout(updatemenus=[{
    'buttons': [
        {'args': [None, {'frame': {'duration': 50, 'redraw': True}, 'fromcurrent': True}],
         'label': 'Play',
         'method': 'animate'},
        {'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
         'label': 'Pause',
         'method': 'animate'}
    ],
    'direction': 'left',
    'pad': {'r': 10, 't': 87},
    'showactive': False,
    'type': 'buttons',
    'x': 0.1,
    'xanchor': 'right',
    'y': 0,
    'yanchor': 'top'
}])

fig.show()
