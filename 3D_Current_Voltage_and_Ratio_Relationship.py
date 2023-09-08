import numpy as np
import pandas as pd
import plotly.express as px

# Constants
emf = 3.200  # EMF of the lithium cell in volts
internal_resistance = 5.00  # Internal resistance in ohms
voltmeter_resistance = 1000.0  # Voltmeter resistance in ohms

# (a) Calculate the current flowing through the circuit
voltage_values = np.linspace(0, emf, 100)
current_values = (emf - voltage_values) / (internal_resistance + voltmeter_resistance)

# (b) Calculate the terminal voltage
terminal_voltage = emf - current_values * internal_resistance

# (c) Calculate the ratio of measured terminal voltage to EMF
ratio = terminal_voltage / emf

# Create a DataFrame to store the data
df = pd.DataFrame({'Voltage (V)': voltage_values, 'Current (A)': current_values, 'Ratio': ratio})

# Create an interactive 3D scatter plot using Plotly Express
fig = px.scatter_3d(df, x='Voltage (V)', y='Current (A)', z='Ratio', color='Ratio', labels={'Ratio': 'Ratio'},
                    title='Current, Voltage, and Ratio Relationship', opacity=0.7, hover_data=['Voltage (V)'])

# Customize the color scale
fig.update_traces(marker=dict(size=5), selector=dict(mode='markers'))

# Add a colorbar
fig.update_layout(coloraxis_colorbar=dict(title='Ratio'))

# Show the plot
fig.show()
