import numpy as np
import pandas as pd
import plotly.graph_objs as go

# Define constants and variables
mu = 0.03  # Linear density in kg/m
length = 2.0  # Length of the string in meters
tension_values = np.linspace(10, 40, 100)  # Tension values in N

# Calculate wave speeds and frequencies
wave_speeds = np.sqrt(tension_values / mu)
frequencies = wave_speeds / length

# Create a list to store animation frames
frames = []

# Create animation frames
for i, tension in enumerate(tension_values):
    frame = go.Frame(
        data=[
            go.Scatter3d(
                x=tension_values[:i+1],
                y=wave_speeds[:i+1],
                z=frequencies[:i+1],
                mode='markers',
                marker=dict(size=5, color='blue')
            )
        ],
        name=f'Tension = {tension} N'
    )
    frames.append(frame)

# Create 3D Visualization using Plotly
fig = go.Figure(
    data=[
        go.Scatter3d(
            x=[tension_values[0]],
            y=[wave_speeds[0]],
            z=[frequencies[0]],
            mode='markers',
            marker=dict(size=5, color='blue')
        )
    ],
    layout=go.Layout(
        scene=dict(
            xaxis_title='Tension (N)',
            yaxis_title='Wave Speed (m/s)',
            zaxis_title='Frequency (Hz)'
        ),
        title='Frequency vs. Tension and Wave Speed',
        margin=dict(l=0, r=0, b=0, t=40),
        updatemenus=[
            {
                'buttons': [
                    {
                        'args': [None, {'frame': {'duration': 150, 'redraw': True}, 'fromcurrent': True}],
                        'label': 'Play',
                        'method': 'animate'
                    },
                    {
                        'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
                        'label': 'Pause',
                        'method': 'animate'
                    }
                ],
                'direction': 'left',
                'pad': {'r': 10, 't': 87},
                'showactive': False,
                'type': 'buttons',
                'x': 0.1,
                'xanchor': 'right',
                'y': 0,
                'yanchor': 'top'
            }
        ],
        sliders=[{
            'active': 0,
            'yanchor': 'top',
            'xanchor': 'left',
            'currentvalue': {
                'font': {'size': 20},
                'prefix': 'Tension: ',
                'visible': True,
                'xanchor': 'right'
            },
            'transition': {'duration': 300, 'easing': 'cubic-in-out'},
            'pad': {'b': 10, 't': 50},
            'len': 0.9,
            'x': 0.1,
            'y': 0,
            'steps': [
                {
                    'args': [
                        [f'Tension = {tension} N'],
                        {
                            'frame': {'duration': 300, 'redraw': True},
                            'mode': 'immediate',
                            'transition': {'duration': 0}
                        }
                    ],
                    'label': f'{tension} N',
                    'method': 'animate'
                }
                for tension in tension_values
            ]
        }]
    ),
    frames=frames
)

fig.show()
