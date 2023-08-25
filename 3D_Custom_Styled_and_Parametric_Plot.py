import plotly.express as px

# Using a custom color palette
fig = px.line(df, x='Time', y=['Voltage', 'Current'], title='Custom Styled Plot')
fig.update_traces(line=dict(color='purple', width=2), mode='lines+markers')
fig.update_layout(title_font=dict(size=24), legend=dict(title='Signal', font=dict(size=18)))

fig.show()

fig = px.scatter_3d(df, x='Time', y='Voltage', z='Current', title='3D Parametric Plot')
fig.show()
