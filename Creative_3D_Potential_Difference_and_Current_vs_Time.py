import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import ipywidgets as widgets
from IPython.display import display, clear_output

# Define parameters
R = 1000  # Ohms
C = 0.001  # Farads
V0 = 10  # Initial voltage (e.g., 10 volts)
tau = R * C  # Time constant

# Create time values
time = np.linspace(0, 5 * tau, 1000)  # Adjust the time range as needed

# Calculate potential difference across the resistor
V_resistor = V0 * np.exp(-time / tau)

# Calculate current
current = V_resistor / R

# Create a DataFrame for easy data manipulation
data = pd.DataFrame({'Time': time, 'Potential Difference (V)': V_resistor, 'Current (A)': current})

# Create an interactive subplot with widgets
fig = make_subplots(rows=2, cols=1, subplot_titles=("Potential Difference vs. Time", "Current vs. Time"))

# Plot potential difference vs. time
line_potential = go.Scatter(x=data['Time'], y=data['Potential Difference (V)'], name='Potential Difference (V)')
line_current = go.Scatter(x=data['Time'], y=data['Current (A)'], name='Current (A)')

fig.add_trace(line_potential, row=1, col=1)
fig.add_trace(line_current, row=2, col=1)

# Customize the layout
fig.update_layout(
    title='Potential Difference and Current vs. Time',
    xaxis=dict(title='Time (s)'),
    yaxis=dict(title='Value'),
    template="plotly_dark",
    showlegend=True,
)

# Add vertical lines to indicate two intervals of τ
for t in [0.5 * tau, 1.5 * tau]:
    fig.add_shape(
        dict(type='line', x0=t, x1=t, y0=0, y1=max(V_resistor),
             line=dict(color='red', dash='dash'), xref='x', yref='y')
    )

# Create interactive widgets
time_slider = widgets.FloatSlider(value=0, min=0, max=max(time), step=0.1, description='Time (s)')
voltage_label = widgets.Label()
current_label = widgets.Label()

# Define a function to update labels based on slider value
def update_labels(change):
    selected_time = change['new']
    voltage_value = np.interp(selected_time, time, V_resistor)
    current_value = np.interp(selected_time, time, current)
    
    voltage_label.value = f'Potential Difference: {voltage_value:.2f} V'
    current_label.value = f'Current: {current_value:.2f} A'

time_slider.observe(update_labels, 'value')

# Display the interactive widgets
display(fig)
widgets.HBox([time_slider, voltage_label, current_label])
