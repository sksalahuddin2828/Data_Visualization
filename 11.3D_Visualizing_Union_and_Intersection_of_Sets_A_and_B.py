import plotly.graph_objects as go

# Convert pandas Series to Python lists for Plotly
set_A_list = set_A.tolist()
set_B_list = set_B.tolist()
union_result_list = union_result.tolist()
intersection_result_list = intersection_result.tolist()

# Create bar charts to visualize sets
fig = go.Figure(data=[
    go.Bar(name='Set A', x=set_A_list, y=[1] * len(set_A_list), orientation='h'),
    go.Bar(name='Set B', x=set_B_list, y=[2] * len(set_B_list), orientation='h')
])

fig.update_layout(title_text='Visualizing Sets A and B',
                  xaxis_title='Elements',
                  yaxis_title='Sets',
                  yaxis=dict(showticklabels=False, showgrid=False, showline=False),
                  showlegend=True)

fig.show()

# Create scatter plots to visualize set operations
fig = go.Figure()

fig.add_trace(go.Scatter(x=union_result_list, y=[1] * len(union_result_list), mode='markers', name='Union'))
fig.add_trace(go.Scatter(x=intersection_result_list, y=[2] * len(intersection_result_list), mode='markers', name='Intersection'))

fig.update_layout(title_text='Visualizing Union and Intersection of Sets A and B',
                  xaxis_title='Elements',
                  yaxis_title='Set Operations',
                  yaxis=dict(tickvals=[1, 2], ticktext=['Union', 'Intersection'], showline=False),
                  showlegend=True)

fig.show()
