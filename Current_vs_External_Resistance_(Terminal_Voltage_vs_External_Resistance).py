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
external_resistance_range = np.arange(0, 2000, 10)  # Varying external resistance in ohms

# Create an empty DataFrame to store results
results = pd.DataFrame(columns=['External Resistance', 'Current', 'Terminal Voltage'])

# Create a function to update the DataFrame
def update_results(resistance):
    # Calculate the current flowing through the circuit
    current = emf / (internal_resistance + resistance)
    
    # Calculate the terminal voltage
    terminal_voltage = emf - current * internal_resistance
    
    # Append results to the DataFrame
    results.loc[len(results)] = [resistance, current, terminal_voltage]

# Perform calculations and update the DataFrame
for resistance in external_resistance_range:
    update_results(resistance)

# Create an animated plot
fig = make_subplots(rows=1, cols=2,
                    subplot_titles=('Current vs. External Resistance', 'Terminal Voltage vs. External Resistance'),
                    specs=[[{'type': 'scatter'}, {'type': 'scatter'}]])

# Add traces for current and terminal voltage
fig.add_trace(go.Scatter(x=results['External Resistance'], y=results['Current'], mode='lines+markers', name='Current', marker=dict(color='blue')), row=1, col=1)
fig.add_trace(go.Scatter(x=results['External Resistance'], y=results['Terminal Voltage'], mode='lines+markers', name='Terminal Voltage', marker=dict(color='green')), row=1, col=2)

# Customize layout and labels
fig.update_xaxes(title_text='External Resistance (Ohms)', row=1, col=1)
fig.update_xaxes(title_text='External Resistance (Ohms)', row=1, col=2)
fig.update_yaxes(title_text='Current (A)', row=1, col=1)
fig.update_yaxes(title_text='Terminal Voltage (V)', row=1, col=2)
fig.update_layout(title='Alkaline Cell Analysis',
                  showlegend=False, template='plotly_dark')

# Display the animated plot
for i in range(len(results)):
    clear_output(wait=True)
    display(fig)
    time.sleep(0.05)

# Display results
display(results)

# Close the animated plot
plt.close()
