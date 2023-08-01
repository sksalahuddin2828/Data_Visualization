import plotly.graph_objects as go

set_A = [1, 2, 3]
set_B = [3, 4, 5]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0.3, 0.7, 0.5],
    y=[0.5, 0.5, 0.5],
    text=['A', 'B', 'A ∩ B'],
    mode='text',
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=[0.3],
    y=[0.5],
    text=['A'],
    mode='text',
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=[0.7],
    y=[0.5],
    text=['B'],
    mode='text',
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=[0.3, 0.7],
    y=[0.5, 0.5],
    text=['A', 'B'],
    mode='text',
    showlegend=False
))

fig.add_shape(type='circle',
              xref='x',
              yref='y',
              x0=0.2,
              y0=0.3,
              x1=0.4,
              y1=0.7,
              fillcolor='blue',
              opacity=0.5)

fig.add_shape(type='circle',
              xref='x',
              yref='y',
              x0=0.6,
              y0=0.3,
              x1=0.8,
              y1=0.7,
              fillcolor='green',
              opacity=0.5)

fig.update_layout(
    title="Interactive Venn Diagram",
    xaxis=dict(range=[0, 1], showgrid=False, zeroline=False),
    yaxis=dict(range=[0, 1], showgrid=False, zeroline=False),
    showlegend=False,
    shapes=[],
    annotations=[]
)

fig.show()
