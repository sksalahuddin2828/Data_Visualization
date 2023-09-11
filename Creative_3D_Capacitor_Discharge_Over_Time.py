import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given values
C = 8.00e-6  # Capacitance (F)
R = 1.00e3   # Resistance (Ω)
V_initial = 10.0e3  # Initial voltage (V)
V_final = 5.00e2    # Final voltage (V)

# Part (a) - Calculate the time constant (τ)
tau = R * C

# Part (b) - Calculate the time it takes to decline to V_final
t = -tau * np.log(V_final / V_initial)

# Create a DataFrame for the voltage decay over time
time_values = np.linspace(0, 3 * tau, 1000)  # Time values
voltage_values = V_initial * np.exp(-time_values / tau)  # Voltage values
df = pd.DataFrame({'Time (s)': time_values, 'Voltage (V)': voltage_values})

# Create a Plotly subplot with two components
fig = make_subplots(rows=2, cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.1,
                    subplot_titles=("Voltage Decay Over Time", "Voltage vs. Time (Log Scale)"))

# Add a line plot for voltage decay
fig.add_trace(go.Scatter(x=df['Time (s)'], y=df['Voltage (V)'],
                         mode='lines', name='Voltage Decay', line=dict(color='blue')))

# Add a semilog plot for voltage vs. time
fig.add_trace(go.Scatter(x=df['Time (s)'], y=df['Voltage (V)'],
                         mode='lines', name='Semilog Voltage', line=dict(color='red')),
              row=2, col=1)

# Customize subplot layouts
fig.update_layout(title_text='Creative Visualization of Capacitor Discharge',
                  xaxis_title='Time (s)', xaxis2_title='Time (s)',
                  yaxis_title='Voltage (V)', yaxis2_title='Voltage (V)',
                  showlegend=False)

# Create a slider for animation
slider_steps = []
for i in range(len(time_values)):
    slider_step = {'args': [
        {'frame': {'duration': 100, 'redraw': True}, 'transition': {'duration': 0},
         'frame': {'duration': 0, 'redraw': False},
         'mode': 'immediate', 'transition': {'duration': 0}}],
        'label': f'{i}',
        'method': 'animate'}
    slider_steps.append(slider_step)

fig.update_layout(sliders=[{
    'steps': slider_steps,
    'active': 0,
    'transition': {'duration': 0},
    'x': 0,
    'xanchor': 'left',
    'y': -0.2,
    'yanchor': 'bottom'
}])

# Print results
print(f"(a) Time Constant (τ): {tau:.4f} seconds")
print(f"(b) Time to Decline to {V_final} V: {t:.4f} seconds")

# Show the interactive Plotly plot
fig.show()
