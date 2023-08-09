import numpy as np
import plotly.graph_objs as go
from sympy import symbols, Eq, solve

# Define symbols
FT = symbols('FT')  # Tension in the string
mu = symbols('mu')  # Linear density
v = symbols('v')    # Wave speed

# Derive the equation for wave speed
equation = Eq(1 / v**2, mu * FT)
wave_speed_equation = solve(equation, v)[0]

# Define values for linear density
linear_density_value = 0.05

# Calculate wave speed values for a range of tension values
tension_range = np.linspace(1, 20, 100)
wave_speed_values = [float(wave_speed_equation.subs([(FT, T), (mu, linear_density_value)])) for T in tension_range]

# Create an animated plot using Plotly
frames = []

for i in range(len(tension_range)):
    frame = go.Frame(
        data=[
            go.Scatter(x=tension_range[:i+1], y=wave_speed_values[:i+1], mode='lines', name='Wave Speed vs Tension')
        ],
        name=f'Frame {i}'
    )
    frames.append(frame)

fig = go.Figure(
    data=[go.Scatter(x=[tension_range[0]], y=[wave_speed_values[0]], mode='lines', name='Wave Speed vs Tension')],
    layout=go.Layout(
        title='Wave Speed vs Tension Animation',
        xaxis=dict(title='Tension'),
        yaxis=dict(title='Wave Speed'),
        showlegend=True
    ),
    frames=frames
)

play_button = {
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

fig.update_layout(updatemenus=[play_button])

slider_steps = []
for i in range(len(tension_range)):
    step = {
        'args': [
            [{'x': [tension_range[:i+1]], 'y': [wave_speed_values[:i+1]]}],
            {'frame': {'duration': 100, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}},
        ],
        'label': f'Frame {i}',
        'method': 'animate',
    }
    slider_steps.append(step)

fig.update_layout(sliders=[{
    'active': 0,
    'steps': slider_steps
}])

fig.show()
