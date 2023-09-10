import numpy as np
import pandas as pd
import plotly.express as px

# Constants
R = 1.0  # Resistance (Ohms)
C = 1.0  # Capacitance (Farads)
V0 = 0.0  # Initial voltage (Volts)

# Time constant
tau = R * C

# Time values
time_values = np.linspace(0, 5 * tau, 500)  # Adjust the time range as needed

# Calculate voltage at each time point using the charging formula
voltage_values = V0 * (1 - np.exp(-time_values / tau))

# Create a Pandas DataFrame
df = pd.DataFrame({'Time (s)': time_values, 'Voltage (V)': voltage_values})

# Calculate the final voltage after two time constants
final_voltage = V0 * (1 - np.exp(-2))

# Create an interactive Plotly line chart
fig = px.line(df, x='Time (s)', y='Voltage (V)', title='Charging of a Capacitor through a Resistor')
fig.update_traces(mode='markers+lines', marker=dict(size=4))
fig.add_annotation(
    text=f'Final Voltage: {final_voltage:.2f} V',
    x=1.5 * tau, y=final_voltage,
    showarrow=True,
    arrowhead=2,
    ax=0,
    ay=-40
)
fig.update_layout(
    xaxis_title='Time (s)',
    yaxis_title='Voltage (V)',
    xaxis=dict(showline=True, showgrid=False),
    yaxis=dict(showline=True, showgrid=False),
    template='plotly_dark'
)
fig.show()
