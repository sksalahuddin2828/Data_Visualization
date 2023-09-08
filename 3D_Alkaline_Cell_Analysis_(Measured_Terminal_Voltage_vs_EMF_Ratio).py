import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Constants
emf = 1.585  # EMF of the alkaline cell in volts
internal_resistance = 0.100  # Internal resistance in ohms
external_resistance = 1000.0  # External resistance in ohms

# (a) Calculate the current flowing through the circuit
current = emf / (internal_resistance + external_resistance)

# (b) Calculate the terminal voltage
terminal_voltage = emf - current * internal_resistance

# (c) Calculate the ratio of measured terminal voltage to EMF
ratio = terminal_voltage / emf

# Create a Pandas DataFrame to organize the data
data = pd.DataFrame({
    'Component': ['EMF', 'Internal Resistance', 'External Resistance', 'Current', 'Terminal Voltage'],
    'Value': [emf, internal_resistance, external_resistance, current, terminal_voltage]
})

# Create an interactive bar chart using Plotly
fig = px.bar(data, x='Component', y='Value', color='Component',
             title='Alkaline Cell Analysis',
             labels={'Value': 'Magnitude'},
             text='Value', template='plotly_dark')

# Customize the layout
fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
fig.update_xaxes(type='category')

# Create a 3D scatter plot using Plotly for the ratio
ratio_data = pd.DataFrame({
    'Ratio': [ratio]
})

ratio_fig = px.scatter_3d(ratio_data, x=['Measured Terminal Voltage / EMF'], y=[1], z=['Ratio'],
                          title='Measured Terminal Voltage vs. EMF Ratio',
                          labels={'x': 'Ratio'},
                          template='plotly_dark')

# Customize the layout of the 3D plot
ratio_fig.update_layout(scene=dict(xaxis_title='Measured Terminal Voltage / EMF',
                                   yaxis_title='',
                                   zaxis_title='Ratio'))

# Display the interactive plots
fig.show()
ratio_fig.show()

# Display results
print(f'(a) Current Flowing: {current:.2f} A')
print(f'(b) Terminal Voltage: {terminal_voltage:.2f} V')
print(f'(c) Ratio of Measured Terminal Voltage to EMF: {ratio:.2f}')
