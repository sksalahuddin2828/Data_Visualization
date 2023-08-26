import numpy as np
import pandas as pd
import plotly.graph_objects as go
from IPython.display import display
import ipywidgets as widgets

# Create some sample data for demonstration
t = np.linspace(0, 10, 100)
I = np.sin(t)

df_current = pd.DataFrame({'Time': t, 'Current': I})

frames = [go.Frame(data=[go.Scatter(x=df_current['Time'][:i+1], y=df_current['Current'][:i+1], mode='lines+markers')]) for i in range(len(df_current))]

fig_animated_current = go.Figure(
    data=[go.Scatter(x=[], y=[], mode='lines+markers')],
    layout=go.Layout(
        xaxis=dict(range=[0, 10]),
        yaxis=dict(range=[-1.5, 1.5]),
        title='Animated Current vs. Time'
    ),
    frames=frames
)

fig_animated_current.update_layout(
    updatemenus=[
        {
            'buttons': [
                {
                    'args': [None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}],
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
        }
    ],
    sliders=[{
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 20},
            'prefix': 'Time:',
            'visible': True,
            'xanchor': 'right',
        },
        'transition': {'duration': 300, 'easing': 'cubic-in-out'},
        'pad': {'b': 10, 't': 50},
        'len': 0.9,
        'x': 0.1,
        'steps': [{
            'args': [[f.name], {'frame': {'duration': 300, 'redraw': True}, 'transition': {'duration': 0}}],
            'label': f'{i:.2f}',
            'method': 'animate',
        } for i, f in enumerate(fig_animated_current.frames)]
    }]
)

display(fig_animated_current)
