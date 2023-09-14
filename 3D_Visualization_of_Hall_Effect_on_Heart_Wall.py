import numpy as np
import plotly.graph_objs as go
import pandas as pd
import sympy as sp
from sympy.abc import L, v, B, t, E
from sympy import Eq

# Constants
L_val = 0.075  # Length of the wire (meters)
v_val = 0.1  # Velocity of the wire (m/s)
B_val = 1.5  # Magnetic field strength (Tesla)

# Time values
t_values = np.linspace(0, 1, 100)

# Calculate the induced Hall voltage
E_values = v_val * B_val  # Electric field induced (Hall voltage)

# Create a DataFrame for the wire's motion
data = pd.DataFrame({'Time (s)': t_values, 'Position (m)': L_val * t_values, 'Hall Voltage (V)': E_values})

# Create a 3D animation of the wire's motion and magnetic field using Plotly
trace_wire = go.Scatter3d(
    x=data['Position (m)'],
    y=np.zeros_like(t_values),
    z=np.zeros_like(t_values),
    mode='lines',
    line=dict(width=4, color='blue'),
    name='Wire Path'
)

trace_field = go.Cone(
    x=[0],
    y=[0],
    z=[0],
    u=[0],
    v=[0],
    w=[B_val],
    sizemode='absolute',
    sizeref=0.1,
    colorscale='Reds',
    showscale=True,
    opacity=0.8,
    name='Magnetic Field'
)

layout_3d = go.Layout(
    title='3D Visualization of Hall Effect on Heart Wall',
    scene=dict(
        xaxis=dict(title='Position (m)'),
        yaxis=dict(title='Y-Axis'),
        zaxis=dict(title='Z-Axis'),
    )
)

fig_3d = go.Figure(data=[trace_wire, trace_field], layout=layout_3d)

# Create an interactive line plot for Hall voltage vs. time using Plotly
trace_hall_voltage = go.Scatter(
    x=t_values,
    y=np.full_like(t_values, E_values),
    mode='lines',
    line=dict(width=2, color='green'),
    name='Hall Voltage (V)'
)

layout_line = go.Layout(
    title='Hall Voltage vs. Time',
    xaxis=dict(title='Time (s)'),
    yaxis=dict(title='Hall Voltage (V)'),
)

fig_line = go.Figure(data=[trace_hall_voltage], layout=layout_line)

# Create mathematical expressions using SymPy
hall_eq = Eq(E, v * B)
sp.init_printing()

# Display the mathematical expressions
display(hall_eq)

# Show interactive plots
fig_3d.show()
fig_line.show()
