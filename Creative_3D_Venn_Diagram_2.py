import pandas as pd
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def union_sets(set1, set2):
    return set1.union(set2)

def intersection_sets(set1, set2):
    return set1.intersection(set2)

def difference_sets(set1, set2):
    return set1.difference(set2)

def complement_set(universal_set, set1):
    return universal_set.difference(set1)

def cardinality_set(set1):
    return len(set1)

def plot_venn_diagram(set1, set2):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=[0], y=[0],
                             mode='markers',
                             marker=dict(size=0.1, color='white'))
                 )

    fig.add_trace(go.Scatter(x=[0.5], y=[0],
                             mode='markers',
                             marker=dict(size=0.1, color='white'))
                 )

    fig.add_trace(go.Scatter(x=[0.25], y=[0],
                             mode='markers',
                             marker=dict(size=150, color='blue', opacity=0.3),
                             text='A',
                             showlegend=False)
                 )

    fig.add_trace(go.Scatter(x=[0.75], y=[0],
                             mode='markers',
                             marker=dict(size=150, color='red', opacity=0.3),
                             text='B',
                             showlegend=False)
                 )

    fig.add_trace(go.Scatter(x=[0.5], y=[0],
                             mode='markers',
                             marker=dict(size=70, color='purple', opacity=0.3),
                             text='A ∩ B',
                             showlegend=False)
                 )

    fig.add_trace(go.Scatter(x=[0.65], y=[0],
                             mode='markers',
                             marker=dict(size=150, color='purple', opacity=0.3),
                             text='A - B',
                             showlegend=False)
                 )

    fig.add_trace(go.Scatter(x=[0.35], y=[0],
                             mode='markers',
                             marker=dict(size=150, color='purple', opacity=0.3),
                             text='B - A',
                             showlegend=False)
                 )

    fig.update_layout(
        title='Venn Diagram',
        shapes=[
            dict(type='circle',
                 xref='x', yref='y',
                 x0=0, y0=0, x1=0.5, y1=1,
                 line_color='blue'),
            dict(type='circle',
                 xref='x', yref='y',
                 x0=0.5, y0=0, x1=1, y1=1,
                 line_color='red')
        ],
        annotations=[
            dict(x=0.25, y=0.2,
                 xref='x', yref='y',
                 text='A', showarrow=False),
            dict(x=0.75, y=0.2,
                 xref='x', yref='y',
                 text='B', showarrow=False),
            dict(x=0.5, y=0.2,
                 xref='x', yref='y',
                 text='A ∩ B', showarrow=False),
            dict(x=0.65, y=0.2,
                 xref='x', yref='y',
                 text='A - B', showarrow=False),
            dict(x=0.35, y=0.2,
                 xref='x', yref='y',
                 text='B - A', showarrow=False),
        ]
    )

    fig.show()

def plot_3d_visualization():
    # Example 3D Visualization with matplotlib
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Define a parametric curve
    t = np.linspace(0, 10, 100)
    x = np.cos(t)
    y = np.sin(t)
    z = t

    # Plot the 3D curve
    ax.plot(x, y, z, label='Parametric Curve')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_zlabel('Z-axis')
    plt.title('3D Parametric Curve')
    plt.legend()
    plt.show()

def display_math_expression():
    x, y = sp.symbols('x y')
    expr = sp.cos(x) + sp.sin(y)
    sp.pprint(expr)

# Example usage
universal_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

print("Union:", union_sets(set1, set2))
print("Intersection:", intersection_sets(set1, set2))
print("Difference (A - B):", difference_sets(set1, set2))
print("Difference (B - A):", difference_sets(set2, set1))

print("Complement of Set A:", complement_set(universal_set, set1))
print("Cardinality of Set A:", cardinality_set(set1))

plot_venn_diagram(set1, set2)
plot_3d_visualization()
display_math_expression()
