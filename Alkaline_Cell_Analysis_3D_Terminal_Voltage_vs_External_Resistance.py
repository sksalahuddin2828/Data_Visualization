import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
from IPython.display import display, clear_output
import time

# Constants
emf = 1.585  # EMF of the alkaline cell in volts
internal_resistance = 0.100  # Internal resistance in ohms
external_resistance = 1000.0  # External resistance in ohms

# Create a Pandas DataFrame to organize the data
data = pd.DataFrame({
    'Component': ['EMF', 'Internal Resistance', 'External Resistance'],
    'Value': [emf, internal_resistance, external_resistance]
})

# Create an interactive bar chart using Plotly
fig = px.bar(data, x='Component', y='Value', color='Component',
             title='Alkaline Cell Analysis',
             labels={'Value': 'Magnitude'},
             text='Value', template='plotly_dark')

# Customize the layout
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_xaxes(type='category')

# Create an animated plot to show how terminal voltage changes with varying external resistance
external_resistance_range = np.arange(0, 2000, 10)
terminal_voltages = []

for resistance in external_resistance_range:
    # Calculate the current flowing through the circuit
    current = emf / (internal_resistance + resistance)
    
    # Calculate the terminal voltage
    terminal_voltage = emf - current * internal_resistance
    
    terminal_voltages.append(terminal_voltage)
    
    # Update the animated plot
    clear_output(wait=True)
    
    # Create a new figure for the animated plot
    fig_anim = make_subplots(rows=1, cols=2,
                            subplot_titles=('Alkaline Cell Analysis', 'Terminal Voltage vs. External Resistance'),
                            specs=[[{'type': 'bar'}, {'type': 'scatter'}]])
    
    # Add the bar chart to the animated figure
    fig_anim.add_trace(go.Bar(x=data['Component'], y=data['Value'], marker_color='dodgerblue',
                         text=data['Value'], name='Magnitude'), row=1, col=1)
    
    # Add the scatter plot to the animated figure
    fig_anim.add_trace(go.Scatter(x=external_resistance_range, y=terminal_voltages,
                             mode='lines+markers', name='Terminal Voltage',
                             marker=dict(color='limegreen')),
                  row=1, col=2)
    
    fig_anim.update_xaxes(type='category', row=1, col=1)
    fig_anim.update_yaxes(title_text='Magnitude', row=1, col=1)
    fig_anim.update_xaxes(title_text='External Resistance (Ohms)', row=1, col=2)
    fig_anim.update_yaxes(title_text='Terminal Voltage (V)', row=1, col=2)
    
    # Display the animated plot
    display(fig_anim)
    time.sleep(0.01)

# Display results
print(f'(a) Current Flowing: {current:.2f} A')
print(f'(b) Terminal Voltage: {terminal_voltage:.2f} V')

# Close the animated plot
plt.close()
