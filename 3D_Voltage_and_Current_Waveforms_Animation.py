import numpy as np
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

# Create a subplot
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.2,
                    subplot_titles=("Voltage Waveform", "Current Waveform"))

# Add voltage waveform trace
trace_voltage = go.Scatter(x=time, y=voltage_waveform, mode='lines', name='Voltage', line=dict(color='blue'))
fig.add_trace(trace_voltage, row=1, col=1)

# Add current waveform trace
trace_current = go.Scatter(x=time, y=current_waveform, mode='lines', name='Current', line=dict(color='orange'))
fig.add_trace(trace_current, row=2, col=1)

# Update x-axis and y-axis labels
fig.update_xaxes(title_text="Time (s)", row=2, col=1)
fig.update_yaxes(title_text="Voltage (V)", row=1, col=1)
fig.update_yaxes(title_text="Current (A)", row=2, col=1)

# Add dynamic equations as annotations
equation_voltage = f'Voltage = {voltage_peak:.2f} sin({frequency}πt) V'
equation_current = f'Current = Voltage / Resistance = {voltage_peak:.2f} / {resistance:.2f} sin({frequency}πt) A'

annotation_voltage = dict(
    x=0.8, y=0.9, xref='paper', yref='paper',
    text=equation_voltage,
    showarrow=False,
    font=dict(size=12),
    bgcolor='rgba(255, 255, 255, 0.6)',
    bordercolor='rgba(0, 0, 0, 0.6)',
    borderwidth=1
)

annotation_current = dict(
    x=0.8, y=0.9, xref='paper', yref='paper',
    text=equation_current,
    showarrow=False,
    font=dict(size=12),
    bgcolor='rgba(255, 255, 255, 0.6)',
    bordercolor='rgba(0, 0, 0, 0.6)',
    borderwidth=1
)

fig.update_layout(annotations=[annotation_voltage], updatemenus=[dict(type='buttons', showactive=False,
                                                                x=0.1, y=1.15, xanchor='left', yanchor='top',
                                                                buttons=[dict(label='Toggle Equations',
                                                                              method='relayout',
                                                                              args=[{'annotations': [annotation_voltage, annotation_current]}
                                                                                    ])
                                                                         ])])

# Create animation function
def update_trace(frame):
    trace_voltage.y = voltage_waveform[:frame]
    trace_current.y = current_waveform[:frame]
    return [trace_voltage, trace_current]

# Create the animated figure
animated_fig = go.Figure(fig, frames=[go.Frame(data=update_trace(f)) for f in range(2, len(time), 2)])
animated_fig.update_layout(title="Voltage and Current Waveforms Animation", showlegend=False)

# Show the animated plot
animated_fig.show()
