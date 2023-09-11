import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Constants
R = 1.0  # Resistance (Ohms)
C = 1.0  # Capacitance (Farads)
Q0 = 1.0  # Initial charge (Coulombs)
tau = R * C  # Time constant

# Time values
t = np.linspace(0, 5 * tau, 500)

# Charge functions for charging and discharging
Q_charging = Q0 * (1 - np.exp(-t / tau))
Q_discharging = Q0 * np.exp(-t / tau)

# Create Pandas DataFrame
df = pd.DataFrame({'Time (s)': t, 'Charge Charging (C)': Q_charging, 'Charge Discharging (C)': Q_discharging})

# Create 3D scatter plots for charging and discharging
scatter_charging = go.Scatter3d(x=df['Time (s)'], y=df['Time (s)'], z=df['Charge Charging (C)'],
                                 mode='lines', line=dict(color='blue'), name='Charge')
scatter_discharging = go.Scatter3d(x=df['Time (s)'], y=df['Time (s)'], z=df['Charge Discharging (C)'],
                                   mode='lines', line=dict(color='red'), name='Charge')

# Create two separate figures for charging and discharging
fig_charging = go.Figure(data=[scatter_charging])
fig_discharging = go.Figure(data=[scatter_discharging])

# Update layout for both figures
fig_charging.update_layout(scene=dict(xaxis_title='Time (s)', yaxis_title='Time (s)', zaxis_title='Charge (C)'),
                            title_text="Capacitor Charging")
fig_discharging.update_layout(scene=dict(xaxis_title='Time (s)', yaxis_title='Time (s)', zaxis_title='Charge (C)'),
                              title_text="Capacitor Discharging")

# Display both figures side by side
fig_charging.show()
fig_discharging.show()
