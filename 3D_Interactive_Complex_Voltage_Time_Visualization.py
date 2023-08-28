import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given data
frequency = 60  # Hz
Vrms = 1.0      # Root Mean Square voltage

# Calculate time periods
T = 1 / frequency
t_values = np.linspace(0, 2*T, 1000)  # Time values for two periods

# Instantaneous voltage functions
voltage = lambda t: Vrms * np.sin(2 * np.pi * frequency * t)
voltage_negative = lambda t: -Vrms * np.sin(2 * np.pi * frequency * t)

# Calculate times when voltage equals Vrms and -Vrms
t_equal_Vrms = t_values[np.isclose(voltage(t_values), Vrms, atol=1e-2)]
t_equal_negative_Vrms = t_values[np.isclose(voltage_negative(t_values), -Vrms, atol=1e-2)]

# Equation for the AC voltage
voltage_equation = f'Voltage(t) = {Vrms:.2f} * sin(2π * {frequency:.2f} * t)'

# Create a DataFrame for visualization
data = pd.DataFrame({'Time': t_values, 'Voltage': voltage(t_values)})

# Create a more complex function for animation
complex_function = lambda t: 0.8 * np.sin(2 * np.pi * frequency * t) + 0.4 * np.sin(4 * np.pi * frequency * t)
complex_voltage_equation = f'Voltage(t) = 0.8 * sin(2π * {frequency:.2f} * t) + 0.4 * sin(4π * {frequency:.2f} * t)'
complex_voltage = complex_function(t_values)

# Animated plot using Plotly with the new complex function
fig_complex_animated = px.line(x=t_values, y=complex_voltage, title='Animated Complex Voltage-Time Visualization',
                               labels={'x': 'Time', 'y': 'Voltage'})

fig_complex_animated.update_traces(mode='lines+markers')
fig_complex_animated.update_layout(updatemenus=[dict(type='buttons', showactive=False,
                                      buttons=[dict(label='Play',
                                                    method='animate',
                                                    args=[None, {'frame': {'duration': 50, 'redraw': True}, 'fromcurrent': True}]),
                                               dict(label='Pause',
                                                    method='animate',
                                                    args=[[None], {'frame': {'duration': 0, 'redraw': True}, 'mode': 'immediate', 'transition': {'duration': 0}}])])])

# Interactive plot with points and annotations
fig_interactive_enhanced = go.Figure()

fig_interactive_enhanced.add_trace(go.Scatter(x=data['Time'], y=complex_voltage, mode='lines', name='Voltage'))
fig_interactive_enhanced.add_trace(go.Scatter(x=t_equal_Vrms, y=np.full_like(t_equal_Vrms, Vrms),
                                              mode='markers', name='Voltage = Vrms', marker=dict(color='red', size=8)))
fig_interactive_enhanced.add_trace(go.Scatter(x=t_equal_negative_Vrms, y=np.full_like(t_equal_negative_Vrms, -Vrms),
                                              mode='markers', name='Voltage = -Vrms', marker=dict(color='green', size=8)))

# Adding annotations
for t in t_equal_Vrms:
    fig_interactive_enhanced.add_annotation(x=t, y=Vrms,
                                            text="Voltage = Vrms", showarrow=True, arrowhead=1)
for t in t_equal_negative_Vrms:
    fig_interactive_enhanced.add_annotation(x=t, y=-Vrms,
                                            text="Voltage = -Vrms", showarrow=True, arrowhead=1)

fig_interactive_enhanced.update_layout(title='Interactive Complex Voltage-Time Visualization',
                                       xaxis_title='Time', yaxis_title='Voltage')
