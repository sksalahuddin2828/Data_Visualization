import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sympy import symbols, Eq, solve
from scipy.constants import Boltzmann

# Generate voltage values
voltages = np.linspace(100, 150, 50)

# Calculate corresponding powers using P = V^2 / R
powers = (voltages ** 2) / resistance

# Create a Plotly line plot
fig_power_voltage = px.line(x=voltages, y=powers, labels={'x': 'Voltage (V)', 'y': 'Power (W)'},
                            title='Power Output vs Voltage')

# Add equation annotation
equation_text = f'Power = Voltage^2 / Resistance\nResistance = {resistance:.2f} ohms'
fig_power_voltage.add_annotation(x=130, y=500, text=equation_text, showarrow=False)
fig_power_voltage.show()

# Generate temperature values
temperatures = np.linspace(20, 800, 50)

# Calculate corresponding resistances at different temperatures
resistances_temp = rho_20 * (1 + alpha * (temperatures - 20))

# Calculate corresponding lengths using R = ρ * (L / A)
lengths_temp = resistances_temp * cross_sectional_area_m2 / resistivity_operating

# Create a Plotly line plot
fig_length_temperature = px.line(x=temperatures, y=lengths_temp, labels={'x': 'Temperature (°C)', 'y': 'Length (m)'},
                                 title='Length vs Operating Temperature')

# Add theoretical explanation annotation
theory_text = ("As temperature increases, the wire's resistance also increases due to the positive\n"
               "temperature coefficient of resistivity. This results in a longer wire to maintain\n"
               "the same power output.")
fig_length_temperature.add_annotation(x=400, y=0.005, text=theory_text, showarrow=False)
fig_length_temperature.show()

# Create a meshgrid of resistance and length values
resistance_mesh, length_mesh = np.meshgrid(resistance_values, length_values)
power_mesh = (initial_voltage ** 2) / resistance_mesh

# Create an interactive 3D surface plot with animation using Plotly
fig_3d_surface_animation = go.Figure(data=[go.Surface(z=power_mesh, x=resistance_mesh, y=length_mesh)])
fig_3d_surface_animation.update_layout(scene=dict(xaxis_title='Resistance (ohms)', yaxis_title='Length (m)',
                                                  zaxis_title='Power (W)'),
                                       title='Power Output vs Resistance and Length')

# Add animation frames
frames = [go.Frame(data=[go.Surface(z=power_mesh, x=resistance_mesh, y=length_mesh)] +
                          [go.Scatter3d(x=[resistance], y=[length], z=[power], mode='markers',
                                        marker=dict(size=10, color='red'))],
                   name=f'Frame {i}') for i, (resistance, length, power) in enumerate(zip(resistance_values, length_values, powers))]

# Create animation sequence
animation_sequence = []
for i in range(len(frames)):
    frame = go.Frame(data=frames[i].data, name=frames[i].name)
    animation_sequence.append(frame)

# Add slider
fig_3d_surface_animation.frames = animation_sequence
slider_steps = []
for i in range(len(animation_sequence)):
    step = dict(method="animate", args=[f'Frame {i}'], label=str(i))
    slider_steps.append(step)
slider = [dict(steps=slider_steps)]
fig_3d_surface_animation.update_layout(updatemenus=[dict(type="buttons", showactive=False,
                                                         buttons=[dict(label="Play",
                                                                       method="animate",
                                                                       args=[None, {"frame": {"duration": 1000, "redraw": True},
                                                                                   "fromcurrent": True,
                                                                                   "transition": {"duration": 300,
                                                                                                  "easing": "quadratic-in-out"}}]),
                                                                  dict(label="Pause",
                                                                       method="animate",
                                                                       args=[[None], {"frame": {"duration": 0, "redraw": True},
                                                                                     "mode": "immediate",
                                                                                     "transition": {"duration": 0}}])])],
                                       sliders=slider)
fig_3d_surface_animation.show()
