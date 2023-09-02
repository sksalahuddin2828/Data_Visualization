import numpy as np
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import sympy as sp

# Define resistor values and configurations
resistors = [10, 20]  # Ohms
configurations = ['Series', 'Parallel']

# Define voltage source
voltage_source = 5  # Volts

# Create a symbolic variable for current (I)
I = sp.symbols('I')

# Calculate total resistance for series and parallel configurations
total_resistance_series = sum(resistors)
total_resistance_parallel = 1 / sum([1 / R for R in resistors])

# Calculate current for series and parallel configurations using Ohm's Law (V = IR)
current_series = voltage_source / total_resistance_series
current_parallel = voltage_source / total_resistance_parallel

# Create a figure with two subplots (3D visualization and current flow animation)
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'scatter3d'}, {'type': 'scatter'}]])

# Create 3D visualization of resistors
x_positions = np.cumsum([0] + resistors)
y_positions = np.zeros(len(resistors))
z_positions = np.zeros(len(resistors))
resistor_names = [f'Resistor {i+1}' for i in range(len(resistors))]

fig.add_trace(go.Scatter3d(x=x_positions, y=y_positions, z=z_positions, mode='markers+text',
                           marker=dict(size=10, color='blue'),
                           text=resistor_names, textposition='bottom center', name='Resistors'))

fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'),
                  scene_aspectmode='cube', title='Resistor Configuration')

# Create animation of current flow
time_values = np.linspace(0, 2, 100)
current_series_values = np.full_like(time_values, current_series)
current_parallel_values = np.full_like(time_values, current_parallel)

# Add traces for current in series and parallel
fig.add_trace(go.Scatter(x=time_values, y=current_series_values, mode='lines', name='Current (Series)', line=dict(color='red')))
fig.add_trace(go.Scatter(x=time_values, y=current_parallel_values, mode='lines', name='Current (Parallel)', line=dict(color='green')))

fig.update_xaxes(title_text='Time (s)', row=1, col=2)
fig.update_yaxes(title_text='Current (A)', row=1, col=2)
fig.update_layout(title='Current Flow Animation')

# Display the interactive plot
fig.show()
