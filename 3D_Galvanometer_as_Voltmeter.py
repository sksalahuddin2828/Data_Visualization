import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Constants
galvanometer_sensitivity = 100e-6  # 100 μA
galvanometer_resistance = 10.0  # 10.0 Ω

# Define a function to calculate resistance for a given voltage
def calculate_resistance(voltage):
    return (voltage / galvanometer_sensitivity) - galvanometer_resistance

# Create a range of voltages for plotting
voltages = np.linspace(0.0, 400.0, 100)

# Calculate corresponding resistances
resistances = calculate_resistance(voltages)

# (a) Full-scale reading of 300 V
full_scale_reading_a = 300.0  # 300 V
resistance_a = calculate_resistance(full_scale_reading_a)

# (b) Full-scale reading of 0.300 V
full_scale_reading_b = 0.300  # 0.300 V
resistance_b = calculate_resistance(full_scale_reading_b)

# Create a Pandas DataFrame for the results
data = {'Voltage (V)': [full_scale_reading_a, full_scale_reading_b],
        'Required Resistance (Ω)': [resistance_a, resistance_b]}
df = pd.DataFrame(data, index=['Scenario (a)', 'Scenario (b)'])

# Create an animated Plotly visualization
fig = make_subplots(rows=1, cols=2, subplot_titles=('Voltage vs. Resistance', 'Required Resistance'))

# Plot voltage vs. resistance
trace1 = go.Scatter(x=voltages, y=resistances, mode='lines', name='Voltage vs. Resistance')
fig.add_trace(trace1, row=1, col=1)
fig.update_xaxes(title_text='Voltage (V)', row=1, col=1)
fig.update_yaxes(title_text='Resistance (Ω)', row=1, col=1)

# Plot required resistance for (a) and (b)
trace2 = go.Bar(x=df.index, y=df['Required Resistance (Ω)'], name='Required Resistance')
fig.add_trace(trace2, row=1, col=2)
fig.update_yaxes(title_text='Required Resistance (Ω)', row=1, col=2)

fig.update_layout(title='Galvanometer as Voltmeter', showlegend=False)

# Print the results
print(df)

# Show the Plotly animation
fig.show()
