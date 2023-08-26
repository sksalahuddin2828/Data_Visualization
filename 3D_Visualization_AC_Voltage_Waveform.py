import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given values
Vrms = 120  # V
Pave = 60.0  # W

# Calculate peak voltage (V0)
V0 = np.sqrt(2) * Vrms

# Calculate peak power (P0)
P0 = 2 * Pave

# Create a time array for AC voltage waveform
time = np.linspace(0, 1, 1000)
voltage = V0 * np.sin(2 * np.pi * time)

# Create a DataFrame for power variations
power_data = {'Power': ['0 W', 'Peak Power (P0)'],
              'Value': [0, P0]}
power_df = pd.DataFrame(power_data)

# Plot AC voltage waveform using Plotly
fig_voltage = px.line(x=time, y=voltage, title='AC Voltage Waveform',
                      labels={'x': 'Time', 'y': 'Voltage (V)'})
fig_voltage.update_xaxes(title_font=dict(size=14), tickfont=dict(size=12))
fig_voltage.update_yaxes(title_font=dict(size=14), tickfont=dict(size=12))
fig_voltage.show()

# Bar chart for power variations using Plotly
fig_power = px.bar(power_df, x='Power', y='Value', color='Power',
                   title='Power Variation')
fig_power.update_xaxes(title_font=dict(size=14), tickfont=dict(size=12))
fig_power.update_yaxes(title_font=dict(size=14), tickfont=dict(size=12))
fig_power.show()

# Create a 3D surface plot for peak power using Plotly Graph Objects
I0_vals = np.linspace(0, 2, 100)
V0_vals = np.linspace(0, V0, 100)
I0, V0_mesh = np.meshgrid(I0_vals, V0_vals)
P0_surface = 2 * I0 * V0_mesh

fig_surface = go.Figure(data=[go.Surface(x=I0_vals, y=V0_vals, z=P0_surface)])
fig_surface.update_layout(title='Peak Power Surface',
                          scene=dict(xaxis_title='Peak Current (I0)',
                                     yaxis_title='Peak Voltage (V0)',
                                     zaxis_title='Peak Power (P0)'))
fig_surface.show()
