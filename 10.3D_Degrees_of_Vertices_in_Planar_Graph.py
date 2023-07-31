import plotly.graph_objects as go

# Visualize the degrees of vertices with Plotly
fig = go.Figure(data=[go.Bar(x=df['Vertex'], y=df['Degree'], marker=dict(color=df['Degree'], colorscale='viridis'))])
fig.update_layout(title='Degrees of Vertices in Planar Graph (Interactive)',
                  xaxis_title='Vertices', yaxis_title='Degree', template='plotly_dark')
fig.show()
