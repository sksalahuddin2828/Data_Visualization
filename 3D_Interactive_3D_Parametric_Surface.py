import numpy as np
import plotly.graph_objects as go
from sympy import symbols, cos, sin, lambdify

u, v = symbols('u v')
x = cos(u) * cos(v)
y = cos(u) * sin(v)
z = sin(u)

u_values = np.linspace(-2 * np.pi, 2 * np.pi, 100)
v_values = np.linspace(-np.pi, np.pi, 100)
u_mesh, v_mesh = np.meshgrid(u_values, v_values)

x_eval = lambdify((u, v), x, 'numpy')
y_eval = lambdify((u, v), y, 'numpy')
z_eval = lambdify((u, v), z, 'numpy')

x_values = x_eval(u_mesh, v_mesh)
y_values = y_eval(u_mesh, v_mesh)
z_values = z_eval(u_mesh, v_mesh)

fig = go.Figure(data=[go.Surface(x=x_values, y=y_values, z=z_values, colorscale='Viridis')])

fig.update_layout(
    title='Interactive 3D Parametric Surface',
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Z',
    ),
)

fig.show()
