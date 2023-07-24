import plotly.graph_objects as go

fig = go.Figure()

# Add the Riemann zeta function on the critical line
fig.add_trace(go.Scatter(x=t_values, y=zeta_values, mode='lines', name='Riemann Zeta Function on Critical Line'))

# Add the zeros of the Riemann zeta function on the critical line
fig.add_trace(go.Scatter(x=zeros, y=[0] * len(zeros), mode='markers', marker=dict(color='red', size=5),
                         name='Zeros on Critical Line'))

fig.update_layout(title='Riemann Zeta Function on the Critical Line',
                  xaxis_title='t',
                  yaxis_title='zeta(1/2 + it)',
                  legend=dict(x=0.8, y=0.1),
                  showlegend=True)

fig.show()
