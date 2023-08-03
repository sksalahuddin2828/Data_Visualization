import plotly.graph_objects as go

# Create a Venn diagram for a + b = b + a
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(255, 100, 100, 0.7)', line=dict(color='black', width=2)), name='a + b'))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(100, 100, 255, 0.7)', line=dict(color='black', width=2)), name='b + a'))
fig.update_layout(title='Commutative Property: a + b = b + a', showlegend=True)
fig.show()

# Create a Venn diagram for a * b = b * a
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(255, 100, 100, 0.7)', line=dict(color='black', width=2)), name='a * b'))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(100, 100, 255, 0.7)', line=dict(color='black', width=2)), name='b * a'))
fig.update_layout(title='Commutative Property: a * b = b * a', showlegend=True)
fig.show()

# Create a Venn diagram for a + 0 = a
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(100, 200, 100, 0.7)', line=dict(color='black', width=2)), name='a + 0'))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(255, 100, 100, 0.7)', line=dict(color='black', width=2)), name='a'))
fig.update_layout(title='Identity Property: a + 0 = a', showlegend=True)
fig.show()

# Create a Venn diagram for a * 1 = a
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(100, 200, 100, 0.7)', line=dict(color='black', width=2)), name='a * 1'))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(255, 100, 100, 0.7)', line=dict(color='black', width=2)), name='a'))
fig.update_layout(title='Identity Property: a * 1 = a', showlegend=True)
fig.show()

# Create a Venn diagram for a + a' = 1
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(100, 100, 255, 0.7)', line=dict(color='black', width=2)), name='a + a\''))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(100, 200, 100, 0.7)', line=dict(color='black', width=2)), name='1'))
fig.update_layout(title='Complemented Law: a + a\' = 1', showlegend=True)
fig.show()

# Create a Venn diagram for a * a' = 0
fig = go.Figure()
fig.add_trace(go.Scatter(x=[0.5], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(100, 100, 255, 0.7)', line=dict(color='black', width=2)), name='a * a\''))
fig.add_trace(go.Scatter(x=[0.6], y=[0.5], mode='markers', marker=dict(size=400, color='rgba(255, 100, 100, 0.7)', line=dict(color='black', width=2)), name='0'))
fig.update_layout(title='Complemented Law: a * a\' = 0', showlegend=True)
fig.show()
