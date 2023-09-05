import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

# Given data
emf = 1.54  # EMF of the cell in volts
internal_resistance = 0.100  # Internal resistance of the cell in ohms
current = 2.00  # Current supplied by the cell in amperes

# (a) Calculate the terminal voltage
voltage_drop = internal_resistance * current
terminal_voltage = emf - voltage_drop

# (b) Calculate the electrical power produced by the cell
power_produced = emf * current

# (c) Calculate the power delivered to the load (circuit)
power_delivered_to_load = terminal_voltage * current

# Create a Pandas DataFrame to store the data
data = {'Parameter': ['Terminal Voltage (V)', 'Power Produced (W)', 'Power Delivered to Load (W)'],
        'Value': [terminal_voltage, power_produced, power_delivered_to_load]}

df = pd.DataFrame(data)

# Display results using Pandas
print("Results:")
print(df)

# Create interactive bar chart using Plotly
fig_bar = px.bar(df, x='Parameter', y='Value', title='Physics Lab Results',
                 labels={'Parameter': 'Parameter', 'Value': 'Value'})
fig_bar.update_traces(marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)',
                      marker_line_width=1.5, opacity=0.6)

# Create a 3D visualization using Plotly
x_values = np.linspace(0, emf, 100)
y_values = np.linspace(0, current, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = X - internal_resistance * Y

fig_3d = go.Figure(data=[go.Surface(z=Z, x=X, y=Y)])
fig_3d.update_layout(scene=dict(zaxis_title='Terminal Voltage (V)',
                                xaxis_title='EMF (V)',
                                yaxis_title='Current (A)'),
                     title='Terminal Voltage vs. EMF and Current')

# Display interactive plots
fig_bar.show()
fig_3d.show()
