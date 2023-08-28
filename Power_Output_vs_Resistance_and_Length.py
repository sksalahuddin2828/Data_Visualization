import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Generate voltage values
voltages = np.linspace(100, 150, 50)

# Calculate corresponding powers using P = V^2 / R
powers = (voltages ** 2) / resistance

# Create a Plotly line plot
fig_power_voltage = px.line(x=voltages, y=powers, labels={'x': 'Voltage (V)', 'y': 'Power (W)'},
                            title='Power Output vs Voltage')
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
fig_length_temperature.show()

# Create a meshgrid of resistance and length values
resistance_mesh, length_mesh = np.meshgrid(resistance_values, length_values)
power_mesh = (initial_voltage ** 2) / resistance_mesh

# Create an interactive 3D surface plot using Plotly
fig_3d_surface = go.Figure(data=[go.Surface(z=power_mesh, x=resistance_mesh, y=length_mesh)])
fig_3d_surface.update_layout(scene=dict(xaxis_title='Resistance (ohms)', yaxis_title='Length (m)',
                                        zaxis_title='Power (W)'),  # Set axis titles within scene
                            title='Power Output vs Resistance and Length')  # Set the overall plot title
fig_3d_surface.show()

