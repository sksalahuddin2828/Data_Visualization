import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import sympy as sp

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

# Create a Plotly subplot figure
fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.05,
                    subplot_titles=("AC Voltage Waveform", "Voltage Crossing Animation"))

# Plot AC voltage waveform
fig.add_trace(go.Scatter(x=t, y=voltage, mode='lines', name='AC Voltage'), row=1, col=1)

# Calculate angular frequency and period
angular_frequency = 2 * np.pi * frequency
period = 1 / frequency

# Create an equation using Sympy
time_sym = sp.symbols('t')
equation = sp.sin(angular_frequency * time_sym)

# Add equation annotation
equation_text = sp.latex(equation)
fig.add_annotation(text=equation_text, x=0.5, y=1.2, showarrow=False, row=1, col=1)

# Add shape annotations and marker points for crossing times
for target_voltage in target_voltages:
    times = crossing_times[target_voltage]
    for crossing_time in times:
        fig.add_shape(type='line', x0=crossing_time, x1=crossing_time,
                      y0=min(voltage), y1=max(voltage),
                      line=dict(color='red', width=2), row=1, col=1)
        fig.add_trace(go.Scatter(x=[crossing_time], y=[target_voltage],
                                 mode='markers', marker=dict(color='red')),
                      row=1, col=1)

# Create an animation of voltage crossing
frames = []
for target_voltage in target_voltages:
    times = crossing_times[target_voltage]
    if len(times) > 0:  # Check if there are crossing times
        max_time = max(times)
        frames.append(go.Frame(data=[go.Scatter(x=[t[idx]], y=[voltage[idx]],
                                                mode='markers', marker=dict(color='blue', size=10))
                                    for idx in range(len(t)) if t[idx] <= max_time],
                               name=f"Frame_{target_voltage:.1f}"))

fig.frames = frames

# Update layout with labels and title
fig.update_layout(title='AC Voltage Waveform and Crossing Points',
                  xaxis_title='Time (s)', yaxis_title='Voltage',
                  showlegend=False)

# Update animation settings
fig.update_layout(updatemenus=[{
    'buttons': [
        {
            'args': [None, {'frame': {'duration': 500, 'redraw': True}, 'fromcurrent': True}],
            'label': 'Play',
            'method': 'animate'
        },
        {
            'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
            'label': 'Pause',
            'method': 'animate'
        }
    ],
    'direction': 'left',
    'pad': {'r': 10, 't': 87},
    'showactive': False,
    'type': 'buttons',
    'x': 0.1,
    'xanchor': 'right',
    'y': 0,
    'yanchor': 'top'
}])

# Add slider for animation frames
slider_steps = []
for idx in range(len(target_voltages)):
    slider_steps.append({
        'args': [
            [f'Frame_{target_voltages[idx]:.1f}'],
            {'frame': {'duration': 300, 'redraw': True}, 'mode': 'immediate'}
        ],
        'label': f'{target_voltages[idx]:.1f}',
        'method': 'animate'
    })

fig.update_layout(sliders=[{
    'active': 0,
    'steps': slider_steps,
    'x': 0.1,
    'xanchor': 'left',
    'y': 0,
    'yanchor': 'top'
}])

# Show the Plotly figure
fig.show()
