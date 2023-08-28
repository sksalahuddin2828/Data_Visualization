import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Generate AC waveform data
frequency = 60
sampling_rate = 1000
duration = 1
t = np.linspace(0, duration, int(sampling_rate * duration), endpoint=False)
voltage = np.sin(2 * np.pi * frequency * t)

# Find crossing times
def find_crossings(signal, target_value):
    crossings = np.where(np.diff(np.sign(signal - target_value)))[0]
    return crossings

target_voltages = [0.5, 1.0, 0.0]
crossing_times = {}
for target_voltage in target_voltages:
    crossings = find_crossings(voltage, target_voltage)
    crossing_times[target_voltage] = t[crossings]

# Create a Plotly figure
fig = go.Figure()

# Plot AC voltage waveform
fig.add_trace(go.Scatter(x=t, y=voltage, mode='lines', name='AC Voltage'))

# Add shape annotations and marker points for crossing times
for target_voltage in target_voltages:
    times = crossing_times[target_voltage]
    for crossing_time in times:
        fig.add_shape(type='line', x0=crossing_time, x1=crossing_time,
                      y0=min(voltage), y1=max(voltage),
                      line=dict(color='red', width=2))
        fig.add_trace(go.Scatter(x=[crossing_time], y=[target_voltage],
                                 mode='markers', marker=dict(color='red')))

# Update layout with labels and title
fig.update_layout(title='AC Voltage Waveform and Crossing Points',
                  xaxis_title='Time (s)', yaxis_title='Voltage',
                  showlegend=True)

# Show the Plotly figure
fig.show()
