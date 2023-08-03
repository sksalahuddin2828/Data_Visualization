import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Create a Venn diagram for a + b = b + a
fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='a + b'))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='b + a'))
fig.update_layout(title='Commutative Property: a + b = b + a')
fig.show()

# Create a Venn diagram for a * b = b * a
fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='a * b'))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='b * a'))
fig.update_layout(title='Commutative Property: a * b = b * a')
fig.show()

# Create a Venn diagram for a + 0 = a
fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='a + 0'))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='a'))
fig.update_layout(title='Identity Property: a + 0 = a')
fig.show()

# Create a Venn diagram for a * 1 = a
fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='a * 1'))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='a'))
fig.update_layout(title='Identity Property: a * 1 = a')
fig.show()

# Create a Venn diagram for a + a' = 1
fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='a + a\''))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='1'))
fig.update_layout(title='Complemented Law: a + a\' = 1')
fig.show()

# Create a Venn diagram for a * a' = 0
fig = make_subplots(rows=1, cols=1)
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='a * a\''))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(0, 0, 0, 0)', line=dict(color='black', width=2)), name='0'))
fig.update_layout(title='Complemented Law: a * a\' = 0')
fig.show()
