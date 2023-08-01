import plotly.graph_objects as go

# Convert Python lists to NumPy arrays for Plotly
set_A_np = np.array(set_A)
set_B_np = np.array(set_B)

# Create bar chart to visualize multisets
fig = go.Figure()
fig.add_trace(go.Bar(x=np.unique(set_A_np), y=np.bincount(set_A_np), name='Set A', marker_color='blue'))
fig.add_trace(go.Bar(x=np.unique(set_B_np), y=np.bincount(set_B_np), name='Set B', marker_color='red'))

fig.update_layout(title_text='Visualizing Multisets A and B',
                  xaxis_title='Elements',
                  yaxis_title='Multiplicity',
                  showlegend=True)

fig.show()

# Create scatter plot to visualize set operations
fig = go.Figure()
fig.add_trace(go.Scatter(x=union_result, y=[1] * len(union_result), mode='markers', name='Union', marker_color='green'))
fig.add_trace(go.Scatter(x=intersection_result, y=[2] * len(intersection_result), mode='markers', name='Intersection', marker_color='orange'))
fig.add_trace(go.Scatter(x=difference_result, y=[3] * len(difference_result), mode='markers', name='Difference', marker_color='purple'))
fig.add_trace(go.Scatter(x=sum_result, y=[4] * len(sum_result), mode='markers', name='Sum', marker_color='brown'))

fig.update_layout(title_text='Visualizing Set Operations',
                  xaxis_title='Elements',
                  yaxis_title='Set Operations',
                  yaxis=dict(tickvals=[1, 2, 3, 4], ticktext=['Union', 'Intersection', 'Difference', 'Sum'], showline=False),
                  showlegend=True)

fig.show()
