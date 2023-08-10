import numpy as np
import plotly.graph_objects as go
import sympy as sp

x, t, A, omega, mu, v = sp.symbols('x t A omega mu v')

# Define given parameters
omega = sp.symbols('omega')
mu = sp.symbols('mu')
v = sp.symbols('v')

x_values = np.linspace(0, 1, 100)

# Define the kinetic energy equation
kinetic_energy = 0.5 * mu * A**2 * omega**2 * v**2 * sp.cos(2 * sp.pi * v * t - 2 * sp.pi * v * x)

# Create a meshgrid for x, t
X, T = np.meshgrid(x_values, np.linspace(0, 1, 100))

# Evaluate kinetic energy for the meshgrid
kinetic_energy_mesh = np.array([[float(kinetic_energy.subs([(A, 1), (omega, 1), (mu, 1), (v, 1), (t, t_val), (x, x_val)])) for x_val in x_values] for t_val in np.linspace(0, 1, 100)])

# Create a 3D plot using Plotly
fig = go.Figure(data=[go.Surface(z=kinetic_energy_mesh, x=X, y=T)])
fig.update_layout(
    title='3D Visualization of Kinetic Energy',
    scene=dict(
        xaxis_title='Position (x)',
        yaxis_title='Time (t)',
        zaxis_title='Kinetic Energy',
    ),
)
fig.show()
