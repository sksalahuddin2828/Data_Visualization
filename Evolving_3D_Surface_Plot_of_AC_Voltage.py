import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Calculate the time for one complete cycle of 400-Hz AC power
frequency = 400  # in Hertz
time_period = 1 / frequency  # in seconds

# Define the symbolic variables and functions
angle, time = sp.symbols('angle time', real=True)
voltage_function = 170 * sp.sin(angle) * sp.exp(-time / (2 * np.pi * frequency))

# Create a numpy function from the symbolic function
voltage_np = sp.lambdify((angle, time), voltage_function, 'numpy')

# Generate angle and time values
angles = np.linspace(0, 2 * np.pi, 100)
times = np.linspace(0, 2 * np.pi / frequency, 100)
angle_grid, time_grid = np.meshgrid(angles, times)
voltages = voltage_np(angle_grid, time_grid)

# Create an evolving 3D surface plot using Plotly
fig_surface = go.Figure()

surface = go.Surface(x=angle_grid, y=time_grid, z=voltages, colorscale='Viridis')
fig_surface.add_trace(surface)

frames = [go.Frame(data=[go.Surface(z=voltage_np(angle_grid, time))], name=f"frame_{i}") for i, time in enumerate(times)]
fig_surface.frames = frames

fig_surface.update_layout(
    title='Evolving 3D Surface Plot of AC Voltage',
    scene=dict(
        xaxis_title='Angle (radians)',
        yaxis_title='Time',
        zaxis_title='Voltage',
    ),
    updatemenus=[{
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
    }],
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
            'args': [
                [f"frame_{i}"],
                {'frame': {'duration': 100, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}},
            ],
            'label': f'{time:.2f}',
            'method': 'animate',
        } for i, time in enumerate(times)],
    }]
)

fig_surface.show()
