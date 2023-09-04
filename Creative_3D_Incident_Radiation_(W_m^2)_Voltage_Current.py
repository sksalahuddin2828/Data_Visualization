import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Constants
incident_radiation = np.linspace(0, 1000, 100)  # Varying incident radiation (W/m^2)
cell_efficiency = 0.15  # Solar cell efficiency (15%)

# Constants for Shockley–Queisser equation
q = 1.60219e-19  # Electron charge (C)
k = 1.38065e-23  # Boltzmann constant (J/K)
T = 298.15  # Temperature in Kelvin (25°C)

# Calculate voltage and current using the Shockley–Queisser limit equation
voltage = np.linspace(0, 0.6, 100)  # Varying voltage (V)
current = np.zeros_like(voltage)

for i, V in enumerate(voltage):
    if V <= 0.6:
        current[i] = (cell_efficiency * incident_radiation[50] * 
                      (np.exp((q * V) / (k * T)) - 1))  # Shockley–Queisser equation

# Calculate power
power = voltage * current

# Create a pandas DataFrame
df = pd.DataFrame({'Incident_Radiation': incident_radiation, 'Voltage': voltage, 'Current': current, 'Power': power})

# Create interactive 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=df['Incident_Radiation'],
    y=df['Voltage'],
    z=df['Current'],
    mode='markers',
    marker=dict(size=8, color=df['Power'], colorscale='Viridis', opacity=0.8),
    text='Power Output'
)])

fig.update_layout(scene=dict(xaxis_title='Incident Radiation (W/m^2)',
                             yaxis_title='Voltage (V)',
                             zaxis_title='Current (A)'),
                  title='Solar Cell Performance',
                  margin=dict(l=0, r=0, b=0, t=40))

# Display analysis results
max_power_idx = df['Power'].idxmax()
max_power_radiation = df.loc[max_power_idx, 'Incident_Radiation']
max_power_voltage = df.loc[max_power_idx, 'Voltage']
max_power_current = df.loc[max_power_idx, 'Current']

# Show the interactive 3D plot
fig.show()

# Display analysis results
print(f"Maximum Power Output: {df['Power'].max()} W")
print(f"Optimal Incident Radiation: {max_power_radiation} W/m^2")
print(f"Optimal Voltage: {max_power_voltage} V")
print(f"Optimal Current: {max_power_current} A")
