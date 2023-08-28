import numpy as np
import pandas as pd
import plotly.express as px

# Given data
frequency = 60  # Hz
Vrms = 1.0      # Root Mean Square voltage

# Calculate time periods
T = 1 / frequency
t_values = np.linspace(0, 2*T, 1000)  # Time values for two periods

# Instantaneous voltage functions
voltage = lambda t: Vrms * np.sin(2 * np.pi * frequency * t)
voltage_negative = lambda t: -Vrms * np.sin(2 * np.pi * frequency * t)

# Create a DataFrame for visualization
data = pd.DataFrame({'Time': t_values, 'Voltage': voltage(t_values)})

# Create animated plot using Plotly
fig_animated = px.line(data, x='Time', y='Voltage', title='Animated Voltage-Time Visualization',
                       labels={'Time': 'Time', 'Voltage': 'Voltage'}, animation_frame='Time')
fig_animated.update_traces(mode='lines+markers')
fig_animated.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                      buttons=[dict(label='Play',
                                                    method='animate',
                                                    args=[None, {'frame': {'duration': 50, 'redraw': True}, 'fromcurrent': True}]),
                                               dict(label='Pause',
                                                    method='animate',
                                                    args=[[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}])])])
fig_animated.show()


import plotly.graph_objects as go

# Create interactive plot with points at times when voltage equals Vrms and -Vrms
fig_interactive = go.Figure()

fig_interactive.add_trace(go.Scatter(x=data['Time'], y=data['Voltage'], mode='lines', name='Voltage'))
fig_interactive.add_trace(go.Scatter(x=t_equal_Vrms, y=np.full_like(t_equal_Vrms, Vrms),
                                     mode='markers', name='Voltage = Vrms', marker=dict(color='red', size=8)))
fig_interactive.add_trace(go.Scatter(x=t_equal_negative_Vrms, y=np.full_like(t_equal_negative_Vrms, -Vrms),
                                     mode='markers', name='Voltage = -Vrms', marker=dict(color='green', size=8)))

fig_interactive.update_layout(title='Interactive Voltage-Time Visualization',
                              xaxis_title='Time', yaxis_title='Voltage')

# Adding annotations
for t in t_equal_Vrms:
    fig_interactive.add_annotation(x=t, y=Vrms,
                                   text="Voltage = Vrms", showarrow=True, arrowhead=1)
for t in t_equal_negative_Vrms:
    fig_interactive.add_annotation(x=t, y=-Vrms,
                                   text="Voltage = -Vrms", showarrow=True, arrowhead=1)

fig_interactive.show()
