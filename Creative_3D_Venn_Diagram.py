import pandas as pd
import plotly.graph_objects as go

def union_sets(set1, set2):
    return set1.union(set2)

def intersection_sets(set1, set2):
    return set1.intersection(set2)

def difference_sets(set1, set2):
    return set1.difference(set2)

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


# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print("Union:", union_sets(set1, set2))
print("Intersection:", intersection_sets(set1, set2))
print("Difference (A - B):", difference_sets(set1, set2))
print("Difference (B - A):", difference_sets(set2, set1))

plot_venn_diagram(set1, set2)
