import numpy as np
import pandas as pd
import plotly.express as px

# Constants
emf = 3.200  # EMF of the lithium cell in volts
voltmeter_resistance = 1000.0  # Voltmeter resistance in ohms

# Create a range of internal resistances
internal_resistances = np.linspace(0, 10, 100)

# Initialize lists to store data
voltage_values = []
current_values = []
ratio_values = []

for internal_resistance in internal_resistances:
    # Calculate the current flowing through the circuit
    current = (emf - 0) / (internal_resistance + voltmeter_resistance)

    # Calculate the terminal voltage
    terminal_voltage = emf - current * internal_resistance

    # Calculate the ratio of measured terminal voltage to EMF
    ratio = terminal_voltage / emf

    voltage_values.append(terminal_voltage)
    current_values.append(current)
    ratio_values.append(ratio)

# Create a DataFrame to store the data
df = pd.DataFrame({'Internal Resistance (Ω)': internal_resistances,
                   'Terminal Voltage (V)': voltage_values,
                   'Current (A)': current_values,
                   'Ratio': ratio_values})

# Create an animated 3D scatter plot using Plotly Express
fig = px.scatter_3d(df, x='Internal Resistance (Ω)', y='Current (A)', z='Terminal Voltage (V)', animation_frame='Ratio',
                    color='Ratio', labels={'Terminal Voltage (V)': 'Voltage (V)', 'Current (A)': 'Current (A)',
                                            'Ratio': 'Ratio'},
                    title='Variation of Current and Terminal Voltage with Internal Resistance',
                    opacity=0.7, hover_data=['Ratio'])

# Add mathematical expressions to the title and labels
fig.update_layout(title_text='Variation of Current and Terminal Voltage with Internal Resistance <br>'
                             'EMF = 3.200 V, Voltmeter Resistance = 1000 Ω',
                  scene=dict(xaxis_title='Internal Resistance (Ω)',
                             yaxis_title='Current (A)',
                             zaxis_title='Terminal Voltage (V)'))

# Customize the color scale
fig.update_traces(marker=dict(size=5), selector=dict(mode='markers'))

# Add a colorbar
fig.update_layout(coloraxis_colorbar=dict(title='Ratio'))

# Show the plot
fig.show()
