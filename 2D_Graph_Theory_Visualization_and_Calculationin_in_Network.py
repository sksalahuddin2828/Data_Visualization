import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import networkx as nx
import sympy as sp

# Mathematical Function and Expression Animation
x_math = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_math = np.sin(x_math)

# Animated mathematical expression using SymPy
t = sp.symbols('t')
expr = sp.sin(t) + sp.cos(2*t)
expr_lambdified = sp.lambdify(t, expr, modules=["numpy"])
t_values = np.linspace(0, 2 * np.pi, 100)

# Graph Theory Visualization
G = nx.random_geometric_graph(10, 0.25)

# Interactive Network Visualization
pos = nx.spring_layout(G)
edge_x = []
edge_y = []
for edge in G.edges():
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])

# Create a subplots layout
fig = make_subplots(rows=2, cols=2, specs=[[{'type': 'scatter'}, {'type': 'scatter'}],
                                           [{'type': 'scatter'}, {'type': 'scatter'}]])

# Add plots to subplots
fig.add_trace(go.Scatter(x=x_math, y=y_math, mode='lines'), row=1, col=1)
fig.add_trace(go.Scatter(x=t_values, y=expr_lambdified(t_values), mode='lines'), row=1, col=2)
fig.add_trace(go.Scatter(x=edge_x, y=edge_y, mode='lines', line=dict(color='blue', width=1)),
              row=2, col=1)
fig.add_trace(go.Scatter(x=list(pos.values()), y=list(pos.values()), mode='markers', text=list(G.nodes)),
              row=2, col=2)

# Update layout for better appearance
fig.update_layout(showlegend=False, width=800, height=800)

# Show the interactive figure
fig.show()
