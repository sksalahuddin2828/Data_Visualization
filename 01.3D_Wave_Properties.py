import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create 3D subplots using Plotly
fig = make_subplots(rows=1, cols=3, specs=[[{'type': 'surface'}, {'type': 'surface'}, {'type': 'surface'}]])

fig.add_trace(go.Surface(x=X, y=T, z=y, colorscale='viridis'), row=1, col=1)
fig.add_trace(go.Surface(x=X, y=T, z=velocity, colorscale='plasma'), row=1, col=2)
fig.add_trace(go.Surface(x=X, y=T, z=acceleration, colorscale='inferno'), row=1, col=3)

fig.update_layout(title='Wave Properties in 3D')
fig.show()
