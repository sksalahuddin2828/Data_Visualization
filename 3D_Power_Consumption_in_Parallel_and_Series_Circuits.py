import numpy as np
import plotly.graph_objects as go

# Constants
V = 12.0  # Voltage in volts
headlight_power = 30.0  # Headlight power in watts
starter_power = 2400.0  # Starter power in watts

# Create a meshgrid of resistance and current values
resistances = np.linspace(1, 100, 100)
currents = np.linspace(0.001, 2, 100)
R, I = np.meshgrid(resistances, currents)

# Resistance calculations
headlight_resistance = V**2 / headlight_power
starter_resistance = V**2 / starter_power

# Calculate power for parallel and series connections
parallel_total_resistance = 1 / ((1 / headlight_resistance) + (1 / R))
parallel_power = (V ** 2 / parallel_total_resistance) * R
series_total_resistance = R + starter_resistance
series_power = (V ** 2 / series_total_resistance) * R

# Create 3D surface plots for power in parallel and series circuits
fig = go.Figure()

# Surface plot for parallel circuit
fig.add_trace(go.Surface(x=resistances, y=currents, z=parallel_power, colorscale='blues', name='Parallel Power'))

# Surface plot for series circuit
fig.add_trace(go.Surface(x=resistances, y=currents, z=series_power, colorscale='reds', name='Series Power'))

# Customize the layout
fig.update_layout(
    title='Power Consumption in Parallel and Series Circuits',
    scene=dict(
        xaxis_title='Resistance (Ohms)',
        yaxis_title='Current (Amps)',
        zaxis_title='Power (Watts)',
        xaxis=dict(range=[1, 100]),
        yaxis=dict(range=[0.001, 2]),
    ),
    scene_camera=dict(
        up=dict(x=0, y=0, z=1),
        center=dict(x=0, y=0, z=0),
        eye=dict(x=1, y=1, z=0.5),
    ),
)

# Add mathematical equations as annotations outside the 3D plot
eq_text = (
    'Mathematical Equations:\n'
    'Parallel Power (W) = (V^2 / R_parallel) * R\n'
    'Series Power (W) = (V^2 / R_series) * R\n'
    'V = 12V, Headlight Power = 30W, Starter Power = 2400W'
)

fig.add_annotation(
    text=eq_text,
    x=1.1,
    y=2.2,
    showarrow=False,
    font=dict(size=12, color='black'),
)

# Show the interactive plot
fig.show()
