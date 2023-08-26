import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given values
Vrms = 120  # V
Pave = 60.0  # W
frequency = 60  # Hz

# Calculate peak voltage (V0)
V0 = np.sqrt(2) * Vrms

# Calculate peak power (P0)
P0 = 2 * Pave

# Calculate RMS current (Irms)
Irms = np.sqrt(Pave)

# Create a time array for AC voltage waveform
num_periods = 5  # Number of AC voltage periods to show in animation
num_frames = 100
time = np.linspace(0, num_periods / frequency, num_frames)
voltage = V0 * np.sin(2 * np.pi * frequency * time)

# Create a phasor diagram
phasor_x = [0, np.real(V0)]
phasor_y = [0, np.imag(V0)]

# Create a DataFrame for power variations
power_data = {'Power': ['0 W', 'Peak Power (P0)'],
              'Value': [0, P0]}
power_df = pd.DataFrame(power_data)

# RMS voltage calculation
Vrms_calculated = np.sqrt(np.mean(voltage ** 2))

# Plot RMS voltage and current
fig_rms = make_subplots(rows=1, cols=2, subplot_titles=('RMS Voltage', 'RMS Current'))

fig_rms.add_trace(go.Indicator(
    mode="number",
    value=Vrms_calculated,
    title="Vrms",
    domain={'row': 1, 'column': 1}
))

fig_rms.add_trace(go.Indicator(
    mode="number",
    value=Irms,
    title="Irms",
    domain={'row': 1, 'column': 2}
))

# Update layout for RMS plots
fig_rms.update_layout(height=300, showlegend=False)

# Animation of AC voltage waveform
fig_voltage_animation = px.line(title='AC Voltage Waveform Animation',
                                labels={'x': 'Time', 'y': 'Voltage (V)'})
for i in range(num_frames):
    frame_title = f'Frame {i + 1}'
    fig_voltage_animation.add_scatter(x=[time[i]], y=[voltage[i]], name=frame_title, mode='markers')

fig_voltage_animation.update_xaxes(title_font=dict(size=14), tickfont=dict(size=12))
fig_voltage_animation.update_yaxes(title_font=dict(size=14), tickfont=dict(size=12))
fig_voltage_animation.update_layout(updatemenus=[{
    'buttons': [
        {
            'args': [None, {'frame': {'duration': 100, 'redraw': True}, 'fromcurrent': True}],
            'label': 'Play',
            'method': 'animate',
        },
        {
            'args': [[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}],
            'label': 'Pause',
            'method': 'animate',
        },
    ],
    'direction': 'left',
    'pad': {'r': 10, 't': 87},
    'showactive': False,
    'type': 'buttons',
    'x': 0.1,
    'xanchor': 'right',
    'y': 0,
    'yanchor': 'top',
}])

frames = [go.Frame(data=[go.Scatter(x=[time[k]], y=[voltage[k]], mode='markers')], name=f'Frame {k + 1}') for k in range(num_frames)]
fig_voltage_animation.frames = frames

# Create a phasor diagram animation
fig_phasor_animation = go.Figure(data=[
    go.Scatter(x=[0, np.real(V0)], y=[0, np.imag(V0)], mode='lines+markers', marker=dict(size=10), name='Voltage Phasor'),
    go.Scatter(x=phasor_x, y=phasor_y, mode='lines', line=dict(dash='dash'), name='Reference')
], layout=go.Layout(title='Phasor Diagram'))

fig_phasor_animation.update_xaxes(title='Real Part')
fig_phasor_animation.update_yaxes(title='Imaginary Part')

# Display the plots
fig_rms.show()
fig_voltage_animation.show()
fig_phasor_animation.show()

# Bar chart for power variations using Plotly
fig_power = px.bar(power_df, x='Power', y='Value', color='Power',
                   title='Power Variation')
fig_power.update_xaxes(title_font=dict(size=14), tickfont=dict(size=12))
fig_power.update_yaxes(title_font=dict(size=14), tickfont=dict(size=12))
fig_power.show()
