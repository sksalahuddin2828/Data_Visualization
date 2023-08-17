import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Generate DataFrame with Values
data = []
for a in np.linspace(1, 10, 10):
    for b in np.linspace(1, 10, 10):
        c = np.sqrt(a**2 + b**2)
        data.append({'a': a, 'b': b, 'c': c})
df = pd.DataFrame(data)

# Create Animation
frames = []
for i, row in df.iterrows():
    frame = go.Frame(
        data=[go.Scatter(x=[0, row['a']], y=[0, row['b']], mode='lines+markers', marker=dict(size=10)),
              go.Scatter(x=[row['a']], y=[row['b']], mode='markers', marker=dict(size=15, color='red'))],
        layout=go.Layout(
            title=f'Pythagorean Theorem: a = {row["a"]}, b = {row["b"]}, c = {row["c"]:.2f}',
            showlegend=False,
            xaxis=dict(range=[0, 12], title='a'),
            yaxis=dict(range=[0, 12], title='b'),
            annotations=[
                go.layout.Annotation(x=row['a'], y=row['b'], xref='x', yref='y',
                                     text=f'c = {row["c"]:.2f}', showarrow=True, arrowhead=2, ax=0, ay=-40),
                go.layout.Annotation(x=row['a'] / 2, y=row['b'] / 2, xref='x', yref='y',
                                     text=f'a = {row["a"]:.2f}', showarrow=False, font=dict(color='blue')),
                go.layout.Annotation(x=row['a'] / 2 + 0.2, y=row['b'] / 2 + 0.2, xref='x', yref='y',
                                     text=f'b = {row["b"]:.2f}', showarrow=False, font=dict(color='blue'))
            ]
        )
    )
    frames.append(frame)

# Create Animation Figure
fig = go.Figure(
    data=[go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=1, color='white'))],  # Invisible point for axes scaling
    frames=frames
)

# Add Start/End Frames
start_frame = go.Frame(data=[go.Scatter(x=[0], y=[0], mode='markers', marker=dict(size=1, color='white'))])
end_frame = go.Frame(data=[go.Scatter(x=[df['a'].max()], y=[df['b'].max()], mode='markers', marker=dict(size=1, color='white'))])
frames_list = list(fig.frames)
frames_list = [start_frame] + frames_list + [end_frame]
fig.frames = frames_list

# Create Summary Table
summary_table = df.copy()
summary_table['c'] = summary_table['c'].apply(lambda x: f'{x:.2f}')
summary_table = summary_table.pivot('a', 'b', 'c').astype(str)

# Set Layout and Animation Settings
fig.update_layout(
    updatemenus=[
        {
            'buttons': [
                {
                    'args': [None, {'frame': {'duration': 200, 'redraw': True}, 'fromcurrent': True}],
                    'label': 'Play',
                    'method': 'animate',
                },
                {
                    'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                    'label': 'Pause',
                    'method': 'animate',
                },
            ],
            'direction': 'left',
            'pad': {'r': 10, 't': 87},
            'showactive': False,
            'type': 'buttons',
            'x': 0.1,
            'xanchor': 'right',
            'y': 0,
            'yanchor': 'top',
        },
    ],
    sliders=[{
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 20},
            'prefix': 'Iteration:',
            'visible': True,
            'xanchor': 'right',
        },
        'transition': {'duration': 300, 'easing': 'cubic-in-out'},
        'pad': {'b': 10, 't': 50},
        'len': 0.9,
        'x': 0.1,
        'y': 0,
    }],
    annotations=[
        go.layout.Annotation(
            x=1.15, y=1,
            xref="paper", yref="paper",
            text="a^2 + b^2 = c^2",
            showarrow=False, font=dict(size=16)
        ),
        go.layout.Annotation(
            x=1.15, y=0.9,
            xref="paper", yref="paper",
            text="The Pythagorean Theorem",
            showarrow=False, font=dict(size=12)
        )
    ]
)

# Show Animation
fig.show()

# Display Summary Table
print("\nSummary Table:")
print(summary_table)
