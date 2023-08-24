import plotly.graph_objects as go

# Example sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Create a Venn diagram using plotly.graph_objects
fig = go.Figure()

# Set sizes
fig.add_trace(go.Scatter(
    x=[0.5, 1.5],
    y=[0.5, 0.5],
    mode='markers',
    marker=dict(size=200 * len(A & B), color='blue', opacity=0.5),
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=[1, 2],
    y=[0.5, 0.5],
    mode='markers',
    marker=dict(size=200 * len(B - A), color='red', opacity=0.5),
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=[0.75],
    y=[0.5],
    mode='markers',
    marker=dict(size=200 * len(A - B), color='green', opacity=0.5),
    showlegend=False
))

# Set layout
fig.update_layout(
    shapes=[
        go.layout.Shape(
            type="circle",
            x0=0,
            y0=0,
            x1=1,
            y1=1,
            line=dict(color='rgba(50, 171, 96, 1)'),
        ),
        go.layout.Shape(
            type="circle",
            x0=1,
            y0=0,
            x1=2,
            y1=1,
            line=dict(color='rgba(255, 0, 0, 1)'),
        ),
    ],
    xaxis=dict(range=[-1, 3]),
    yaxis=dict(range=[-1, 2]),
    showlegend=False,
    title="Custom Venn Diagram"
)

# Show the plot
fig.show()
