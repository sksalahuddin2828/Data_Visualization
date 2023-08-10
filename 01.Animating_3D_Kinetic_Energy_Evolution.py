import numpy as np
import plotly.graph_objects as go
import sympy as sp

# Define symbols for symbolic calculations
x, t, A, omega, mu, v = sp.symbols('x t A omega mu v')

# Define given parameters
omega = sp.symbols('omega')
mu = sp.symbols('mu')
v = sp.symbols('v')

# Define the kinetic energy equation
kinetic_energy = 0.5 * mu * A**2 * omega**2 * v**2 * sp.cos(2 * sp.pi * v * t - 2 * sp.pi * v * x)

# Create a meshgrid for x, t
x_values = np.linspace(0, 1, 100)
t_values = np.linspace(0, 1, 50)
X, T = np.meshgrid(x_values, t_values)

# Evaluate kinetic energy for the meshgrid
kinetic_energy_mesh = np.array([[float(kinetic_energy.subs([(A, 1), (omega, 1), (mu, 1), (v, 1), (t, t_val), (x, x_val)])) for x_val in x_values] for t_val in t_values])

# Create an animated surface plot using Plotly
frames = [go.Frame(data=[go.Surface(z=kinetic_energy_mesh[:i+1, :], x=X, y=T[:i+1, :])]) for i in range(len(t_values))]

fig = go.Figure(data=[go.Surface(z=kinetic_energy_mesh, x=X, y=T)], frames=frames)
fig.update_layout(
    title='Animating Kinetic Energy Evolution',
    scene=dict(
        xaxis_title='Position (x)',
        yaxis_title='Time (t)',
        zaxis_title='Kinetic Energy',
    ),
    updatemenus=[{
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 50, 'redraw': True}, 'fromcurrent': True}],
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
        'y': 0,
    }],
)

fig.show()
