import numpy as np
import plotly.graph_objects as go

# Create a time array
t = np.linspace(0, 2 * np.pi, 100)

# Initialize figure
fig = go.Figure()

# Add fundamental frequency sine wave
fundamental = np.sin(t)
fig.add_trace(go.Scatter(x=t, y=fundamental, mode='lines', name='Fundamental'))

# Add higher harmonics and animate
for i in range(2, 101):  # Change the range to include harmonics from 2 to 100
    harmonic = np.sin(i * t) / i  # Divide by 'i' to normalize amplitude
    fig.add_trace(go.Scatter(x=t, y=harmonic, mode='lines', name=f'Harmonic {i}', visible=False))

# Initialize frames as a list
frames = []
for i in range(2, 101):  # Change the range to include frames from 2 to 100
    frame_data = [
        go.Scatter(x=t[:i+1], y=fundamental[:i+1]),
        go.Scatter(x=t[:i+1], y=np.sum([np.sin(k * t[:i+1]) / k for k in range(2, i+1)], axis=0))
    ]
    frame = go.Frame(data=frame_data, name=f'Frame {i}')
    frames.append(frame)

# Add frames to the figure
fig.frames = frames

# Update animation settings
animation_buttons = [
    dict(label='Play',
         method='animate',
         args=[None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True, 'transition': {'duration': 0}}]),
    dict(label='Pause',
         method='animate',
         args=[[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate', 'transition': {'duration': 0}}])
]

# Add buttons to the animation slider
fig.update_layout(updatemenus=[
    dict(type='buttons',
         showactive=False,
         buttons=animation_buttons,
         x=0.1,
         y=0,
         xanchor='right',
         yanchor='top')
])

# Update layout properties
fig.update_layout(
    sliders=[{
        'steps': [
            {'args': [[f'Frame {k}'], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                                       'transition': {'duration': 0}}],
             'label': str(k),
             'method': 'animate'} for k in range(2, 101)
        ],
        'active': 0,
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 20},
            'prefix': 'Frequency: ',
            'visible': True,
            'xanchor': 'right'
        },
        'len': 0.9,
        'x': 0.1,
        'y': 0,
    }],
    title='Harmonic Animation',
    xaxis_title='Time',
    yaxis_title='Amplitude'
)

# Show the figure
fig.show()
