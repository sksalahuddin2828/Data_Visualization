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
set_A_unique, set_A_counts = np.unique(set_A, return_counts=True)
set_B_unique, set_B_counts = np.unique(set_B, return_counts=True)

# Create bar chart to visualize multisets
fig_bar_chart = go.Figure()
fig_bar_chart.add_trace(go.Bar(
    x=set_A_unique,
    y=set_A_counts,
    name='Set A',
    marker_color='#1f77b4',
    hovertemplate='Element: %{x}<br>Multiplicity: %{y}'
))
fig_bar_chart.add_trace(go.Bar(
    x=set_B_unique,
    y=set_B_counts,
    name='Set B',
    marker_color='#ff7f0e',
    hovertemplate='Element: %{x}<br>Multiplicity: %{y}'
))

fig_bar_chart.update_layout(
    title_text='Visualizing Multisets A and B',
    title_font=dict(size=24, family='Arial'),
    xaxis_title='Elements',
    yaxis_title='Multiplicity',
    font=dict(size=14, family='Arial'),
    showlegend=True,
    legend=dict(font=dict(size=16, family='Arial')),
    plot_bgcolor='rgba(240, 240, 240, 0.95)',
    bargap=0.1
)
fig_bar_chart.show()

# Create animated scatter plot to visualize set operations
fig_scatter_plot = go.Figure()

fig_scatter_plot.add_trace(go.Scatter(
    x=union_result,
    y=[1] * len(union_result),
    mode='markers',
    name='Union',
    marker=dict(size=10, color='#2ca02c', line=dict(width=1, color='#000')),
    hovertemplate='Element: %{x}<br>Operation: Union'
))
fig_scatter_plot.add_trace(go.Scatter(
    x=intersection_result,
    y=[2] * len(intersection_result),
    mode='markers',
    name='Intersection',
    marker=dict(size=10, color='#d62728', line=dict(width=1, color='#000')),
    hovertemplate='Element: %{x}<br>Operation: Intersection'
))
fig_scatter_plot.add_trace(go.Scatter(
    x=difference_result,
    y=[3] * len(difference_result),
    mode='markers',
    name='Difference',
    marker=dict(size=10, color='#9467bd', line=dict(width=1, color='#000')),
    hovertemplate='Element: %{x}<br>Operation: Difference'
))
fig_scatter_plot.add_trace(go.Scatter(
    x=sum_result,
    y=[4] * len(sum_result),
    mode='markers',
    name='Sum',
    marker=dict(size=10, color='#8c564b', line=dict(width=1, color='#000')),
    hovertemplate='Element: %{x}<br>Operation: Sum'
))

# Add animation
frames = [go.Frame(data=[go.Scatter(x=union_result[:i], y=[1] * i, mode='markers',
                                   marker=dict(size=10, color='#2ca02c', line=dict(width=1, color='#000')))],
                  name='Union', traces=[0]) for i in range(1, len(union_result) + 1)]
frames += [go.Frame(data=[go.Scatter(x=intersection_result[:i], y=[2] * i, mode='markers',
                                   marker=dict(size=10, color='#d62728', line=dict(width=1, color='#000')))],
                    name='Intersection', traces=[1]) for i in range(1, len(intersection_result) + 1)]
frames += [go.Frame(data=[go.Scatter(x=difference_result[:i], y=[3] * i, mode='markers',
                                   marker=dict(size=10, color='#9467bd', line=dict(width=1, color='#000')))],
                    name='Difference', traces=[2]) for i in range(1, len(difference_result) + 1)]
frames += [go.Frame(data=[go.Scatter(x=sum_result[:i], y=[4] * i, mode='markers',
                                   marker=dict(size=10, color='#8c564b', line=dict(width=1, color='#000')))],
                    name='Sum', traces=[3]) for i in range(1, len(sum_result) + 1)]

# Add slider
slider = go.layout.Slider(
    active=0,
    yanchor='top',
    xanchor='left',
    currentvalue=dict(font=dict(size=16, family='Arial')),
    bgcolor='rgba(255, 255, 255, 0.7)',
    borderwidth=2,
    bordercolor='#999',
    ticklen=10,
    len=0.9,
    pad=dict(t=20),
    x=0.1,
    y=0
)

fig_scatter_plot.update_layout(
    updatemenus=[dict(type='buttons', showactive=False, buttons=[dict(label='Play',
                                                                     method='animate',
                                                                     args=[None,
                                                                           dict(frame=dict(duration=100,
                                                                                           redraw=True),
                                                                                fromcurrent=True,
                                                                                mode='immediate')]),
                                                                dict(label='Pause',
                                                                     method='animate',
                                                                     args=[[None],
                                                                           dict(frame=dict(duration=0,
                                                                                           redraw=False),
                                                                                mode='immediate')])]),
                 dict(type='buttons', showactive=False, buttons=[dict(label=str(i),
                                                                      method='animate',
                                                                      args=[[str(i)], dict(frame=dict(duration=100,
                                                                                                      redraw=True),
                                                                                           mode='immediate')]) for i in range(1, len(sum_result) + 1)])
    ],
    sliders=[slider],
    title_text='Visualizing Set Operations',
    title_font=dict(size=24, family='Arial'),
    xaxis_title='Elements',
    yaxis_title='Set Operations',
    font=dict(size=14, family='Arial'),
    yaxis=dict(tickvals=[1, 2, 3, 4], ticktext=['Union', 'Intersection', 'Difference', 'Sum'], showline=False),
    showlegend=True,
    legend=dict(font=dict(size=16, family='Arial')),
    plot_bgcolor='rgba(240, 240, 240, 0.95)'
)

# Add frames to the figure
fig_scatter_plot.update(frames=frames)

# Add dropdown menu
slider_steps = [dict(
    args=[{"visible": [t == i for t in range(len(frames))]}, {"title": f"Operation: {frames[i]['name']}"}],
    label=f"Operation: {frames[i]['name']}",
    method="update"
) for i in range(len(frames))]

fig_scatter_plot.update_layout(
    updatemenus=[
        dict(
            type="dropdown",
            active=0,
            buttons=slider_steps,
        )
    ]
)

fig_scatter_plot.show()
