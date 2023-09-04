import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Constants
incident_radiation = np.linspace(0, 1000, 100)  # Varying incident radiation (W/m^2)
cell_efficiency = 0.15  # Solar cell efficiency (15%)

# Constants for Shockley–Queisser equation
q = 1.60219e-19  # Electron charge (C)
k = 1.38065e-23  # Boltzmann constant (J/K)
T = 298.15  # Temperature in Kelvin (25°C)

# Create a pandas DataFrame to store results
df = pd.DataFrame({'Incident_Radiation': incident_radiation})

# Calculate voltage, current, and power for each incident radiation level
for radiation in incident_radiation:
    voltage = np.linspace(0, 0.6, 100)  # Varying voltage (V)
    current = np.zeros_like(voltage)

    for i, V in enumerate(voltage):
        if V <= 0.6:
            current[i] = (cell_efficiency * radiation * 
                          (np.exp((q * V) / (k * T)) - 1))  # Shockley–Queisser equation

    power = voltage * current
    df[f'Voltage_{radiation}'] = voltage
    df[f'Current_{radiation}'] = current
    df[f'Power_{radiation}'] = power

# Create an animation of voltage, current, and power with varying incident radiation
fig = make_subplots(rows=1, cols=3, subplot_titles=("Voltage vs. Radiation", "Current vs. Radiation", "Power vs. Radiation"))

for radiation in incident_radiation:
    voltage_col = f'Voltage_{radiation}'
    current_col = f'Current_{radiation}'
    power_col = f'Power_{radiation}'
    
    fig.add_trace(go.Scatter(x=df['Incident_Radiation'], y=df[voltage_col], name=f'{radiation} W/m^2',
                             mode='lines', showlegend=False), row=1, col=1)
    fig.add_trace(go.Scatter(x=df['Incident_Radiation'], y=df[current_col], name=f'{radiation} W/m^2',
                             mode='lines', showlegend=False), row=1, col=2)
    fig.add_trace(go.Scatter(x=df['Incident_Radiation'], y=df[power_col], name=f'{radiation} W/m^2',
                             mode='lines', showlegend=False), row=1, col=3)


fig.update_layout(title='Solar Cell Performance vs. Incident Radiation',
                  xaxis=dict(title='Voltage (V)', range=[0, 0.6]),
                  yaxis=dict(title='Value'),
                  xaxis2=dict(title='Current (A)', range=[0, 0.6]),
                  xaxis3=dict(title='Incident Radiation (W/m^2)', range=[0, 1000]),
                  yaxis3=dict(title='Power (W)'),
                  showlegend=True)

# Show the animation
fig.update_layout(updatemenus=[dict(type='buttons',
                                    showactive=False,
                                    buttons=[dict(label='Play',
                                                    method='animate',
                                                    args=[None,
                                                          dict(frame=dict(duration=100, redraw=True), fromcurrent=True),
                                                          dict(mode='immediate')]),
                                             dict(label='Pause',
                                                    method='animate',
                                                    args=[[None], dict(mode='immediate')])])])

frames = [go.Frame(data=[go.Scatter(x=[df['Incident_Radiation'][i]], y=[df[f'Voltage_{radiation}'][i]], mode='lines+markers',
                                    marker=dict(size=8, color='red', opacity=0.8),
                                    name=f'{radiation} W/m^2', showlegend=False)], name=str(radiation),
                    layout=dict(title=f'Solar Cell Performance vs. Incident Radiation ({radiation} W/m^2)'))
          for i, radiation in enumerate(incident_radiation)]

fig.update(frames=frames)

# Display the animation
fig.show()
