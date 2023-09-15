import numpy as np
import sympy as sp
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Constants
velocity = 0.1  # 10.0 cm/s converted to m/s
length = 0.1    # 10.0 cm converted to meters
induced_voltage = 0.02  # 20.0 mV converted to V

# Symbols
B = sp.symbols('B')

# Faraday's Law equation
eq = sp.Eq(induced_voltage, B * velocity * length)

# Solve for B
magnetic_field_strength = sp.solve(eq, B)[0]

# Convert the result to a numeric value
magnetic_field_strength_numeric = float(magnetic_field_strength.evalf())

# Create a pandas DataFrame to store data
data = pd.DataFrame({'Distance (m)': np.linspace(0, length, 100)})
data['Magnetic Field (T)'] = magnetic_field_strength_numeric * velocity * data['Distance (m)']

# Create a 3D scatter plot with Plotly
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter3d'}, {'type': 'scatter'}]])
fig.update_layout(scene=dict(aspectmode='cube'))
fig.add_trace(go.Scatter3d(
    x=data['Distance (m)'],
    y=np.zeros_like(data['Distance (m)']),
    z=data['Magnetic Field (T)'],
    mode='lines',
    line=dict(width=5, color='blue'),
    name='Pacemaker Wire',
    showlegend=False
))

# Create a 2D line plot
fig.add_trace(go.Scatter(
    x=data['Distance (m)'],
    y=data['Magnetic Field (T)'],
    mode='lines',
    line=dict(width=2, color='blue'),
    name='Magnetic Field',
))

# Add annotations
annotation_text = f'Magnetic Field Strength: {magnetic_field_strength_numeric:.4f} T'
fig.add_annotation(
    text=annotation_text,
    x=data['Distance (m)'].mean(),
    y=data['Magnetic Field (T)'].max(),
    showarrow=True,
    arrowhead=2,
    arrowsize=1,
)

# Customize layout
fig.update_layout(
    title='Magnetic Field Along Pacemaker Wire',
    xaxis_title='Distance (m)',
    yaxis_title='Magnetic Field (T)',
    scene=dict(
        xaxis_title='Distance (m)',
        yaxis_title='Y',
        zaxis_title='Magnetic Field (T)'
    )
)

# Show the plot
fig.show()
