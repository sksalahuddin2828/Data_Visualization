import numpy as np
import pandas as pd
import plotly.express as px

# Generate time values
t = np.linspace(0, 2*np.pi, 1000)

# Simulate AC voltages and currents
V = 220 * np.sin(2*np.pi*50*t)
I = 2 * np.sin(2*np.pi*50*t - np.pi/6)  # Phase difference of 30 degrees

# Create DataFrame
data = {'Time': t, 'Voltage': V, 'Current': I}
df = pd.DataFrame(data)

# Interactive Lissajous figure using Plotly
fig_lissajous = px.scatter(df, x='Voltage', y='Current', title='Interactive Lissajous Figure')
fig_lissajous.update_traces(marker=dict(size=4), line=dict(width=2))
fig_lissajous.show()

# Phasor diagram with Pandas and Plotly
phasor_data = {'Impedance': [np.complex(220, 0) + 2j*(np.cos(np.pi/6) + 1j*np.sin(np.pi/6))]}
phasor_df = pd.DataFrame(phasor_data)

# Convert complex numbers to magnitudes and angles for polar plot
phasor_df['Magnitude'] = np.abs(phasor_df['Impedance'])
phasor_df['Angle'] = np.angle(phasor_df['Impedance'], deg=True)

fig_phasor = px.scatter_polar(phasor_df, r='Magnitude', theta='Angle', title='Interactive Phasor Diagram')
fig_phasor.update_traces(marker=dict(size=10))
fig_phasor.show()
