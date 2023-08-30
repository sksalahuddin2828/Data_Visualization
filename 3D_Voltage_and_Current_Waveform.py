import numpy as np
import pandas as pd
import sympy as sp
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given data
voltage_peak = 220  # Volts
frequency = 60  # Hz
resistance = resistance_a  # Ohms

# Calculate angular frequency
angular_frequency = 2 * np.pi * frequency

# Create time array
time = np.linspace(0, 1, 1000)  # One period

# Calculate voltage and current waveforms
voltage_waveform = voltage_peak * np.sin(angular_frequency * time)
current_waveform = voltage_waveform / resistance

# Create a DataFrame for waveform data
data = {'Time (s)': time,
        'Voltage (V)': voltage_waveform,
        'Current (A)': current_waveform}
df_waveforms = pd.DataFrame(data)

# Create dynamic equations
equation_voltage = f'Voltage = {voltage_peak:.2f} sin({frequency}πt) V'
equation_current = f'Current = Voltage / Resistance = {voltage_peak:.2f} / {resistance:.2f} sin({frequency}πt) A'

# Create subplots using Plotly
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.2,
                    subplot_titles=("Voltage Waveform", "Current Waveform"))

# Add voltage waveform trace
fig.add_trace(go.Scatter(x=df_waveforms['Time (s)'], y=df_waveforms['Voltage (V)'],
                         mode='lines', name='Voltage', line=dict(color='blue')), row=1, col=1)

# Add current waveform trace
fig.add_trace(go.Scatter(x=df_waveforms['Time (s)'], y=df_waveforms['Current (A)'],
                         mode='lines', name='Current', line=dict(color='orange')), row=2, col=1)

# Update x-axis and y-axis labels
fig.update_xaxes(title_text="Time (s)", row=2, col=1)
fig.update_yaxes(title_text="Voltage (V)", row=1, col=1)
fig.update_yaxes(title_text="Current (A)", row=2, col=1)

# Add dynamic equations as annotations
fig.add_annotation(text=equation_voltage, x=0.7, y=0.9, showarrow=False, row=1, col=1)
fig.add_annotation(text=equation_current, x=0.7, y=0.9, showarrow=False, row=2, col=1)

# Update layout
fig.update_layout(title_text="Voltage and Current Waveforms",
                  height=800, width=800, showlegend=False)

# Show the interactive plot
fig.show()
