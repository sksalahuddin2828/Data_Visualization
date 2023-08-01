import numpy as np
import plotly.graph_objects as go

# Sample data for set_A and set_B
set_A = [1, 2, 2, 3, 4, 4, 4, 5, 5]
set_B = [3, 3, 4, 4, 5, 5, 6, 6, 6]

# Sample set operation results
union_result = sorted(set(set_A + set_B))
intersection_result = sorted(set(set_A).intersection(set_B))
difference_result = sorted(set(set_A).difference(set_B))
sum_result = sorted(set_A + set_B)

# Remove duplicates to get the correct multiplicity counts for the bar chart
set_A_unique = np.unique(set_A)
set_B_unique = np.unique(set_B)

# Create bar chart to visualize multisets
fig_bar_chart = go.Figure()
fig_bar_chart.add_trace(go.Bar(
    x=set_A_unique,
    y=np.bincount(set_A),
    name='Set A',
    marker_color='blue',
    hovertemplate='Element: %{x}<br>Multiplicity: %{y}'
))
fig_bar_chart.add_trace(go.Bar(
    x=set_B_unique,
    y=np.bincount(set_B),
    name='Set B',
    marker_color='red',
    hovertemplate='Element: %{x}<br>Multiplicity: %{y}'
))

fig_bar_chart.update_layout(
    title_text='Visualizing Multisets A and B',
    xaxis_title='Elements',
    yaxis_title='Multiplicity',
    showlegend=True
)
fig_bar_chart.show()

# Create animated scatter plot to visualize set operations
fig_scatter_plot = go.Figure()

fig_scatter_plot.add_trace(go.Scatter(
    x=union_result,
    y=[1] * len(union_result),
    mode='markers',
    name='Union',
    marker_color='green',
    hovertemplate='Element: %{x}<br>Operation: Union'
))
fig_scatter_plot.add_trace(go.Scatter(
    x=intersection_result,
    y=[2] * len(intersection_result),
    mode='markers',
    name='Intersection',
    marker_color='orange',
    hovertemplate='Element: %{x}<br>Operation: Intersection'
))
fig_scatter_plot.add_trace(go.Scatter(
    x=difference_result,
    y=[3] * len(difference_result),
    mode='markers',
    name='Difference',
    marker_color='purple',
    hovertemplate='Element: %{x}<br>Operation: Difference'
))
fig_scatter_plot.add_trace(go.Scatter(
    x=sum_result,
    y=[4] * len(sum_result),
    mode='markers',
    name='Sum',
    marker_color='brown',
    hovertemplate='Element: %{x}<br>Operation: Sum'
))

# Add animation
frames = [go.Frame(data=[go.Scatter(x=union_result[:i], y=[1] * i, mode='markers', marker_color='green')],
                  name='Union', traces=[0]) for i in range(1, len(union_result) + 1)]
frames += [go.Frame(data=[go.Scatter(x=intersection_result[:i], y=[2] * i, mode='markers', marker_color='orange')],
                    name='Intersection', traces=[1]) for i in range(1, len(intersection_result) + 1)]
frames += [go.Frame(data=[go.Scatter(x=difference_result[:i], y=[3] * i, mode='markers', marker_color='purple')],
                    name='Difference', traces=[2]) for i in range(1, len(difference_result) + 1)]
frames += [go.Frame(data=[go.Scatter(x=sum_result[:i], y=[4] * i, mode='markers', marker_color='brown')],
                    name='Sum', traces=[3]) for i in range(1, len(sum_result) + 1)]

# Add buttons to control animation
fig_scatter_plot.update_layout(
    updatemenus=[
        dict(
            type="buttons",
            showactive=False,
            buttons=[dict(label=str(i),
                          method="animate",
                          args=[{"visible": [t == i for t in range(len(frames))]},
                                {"title": f"Operation: {frames[i]['name']}"}]) for i in range(len(frames))]
        )
    ],
    title_text='Visualizing Set Operations',
    xaxis_title='Elements',
    yaxis_title='Set Operations',
    yaxis=dict(tickvals=[1, 2, 3, 4], ticktext=['Union', 'Intersection', 'Difference', 'Sum'], showline=False),
    showlegend=True
)

# Add frames to the figure
fig_scatter_plot.update(frames=frames)

fig_scatter_plot.show()
