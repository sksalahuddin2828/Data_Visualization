import numpy as np
import pandas as pd
import plotly.express as px

# Define circuit parameters
V = 12.0  # Voltage output of the battery
R1 = 1.00
R2 = 6.00
R3 = 13.0

# Calculate circuit quantities
Rs = R1 + R2 + R3
I = V / Rs
V1 = I * R1
V2 = I * R2
V3 = I * R3
P1 = I**2 * R1
P2 = I**2 * R2
P3 = I**2 * R3

# Create DataFrame for voltage data
voltage_data = pd.DataFrame({'Resistor': ['R1', 'R2', 'R3'], 'Voltage (V)': [V1, V2, V3]})

# Create an interactive bar chart for voltage drops
fig_voltage = px.bar(voltage_data, x='Resistor', y='Voltage (V)', color='Resistor',
                     title='Voltage Drops in Resistors', labels={'Resistor': 'Resistor Number'})

fig_voltage.update_traces(marker_line_width=2, marker_line_color="black")
fig_voltage.update_layout(xaxis_title="Resistor Number", yaxis_title="Voltage (V)", showlegend=False)

# Create DataFrame for power data
power_data = pd.DataFrame({'Resistor': ['R1', 'R2', 'R3'], 'Power (W)': [P1, P2, P3]})

# Create an interactive pie chart for power dissipation
fig_power = px.pie(power_data, names='Resistor', values='Power (W)',
                   title='Power Dissipation in Resistors', hole=0.4)

fig_power.update_traces(textinfo='percent+label', pull=[0, 0.2, 0], 
                        marker=dict(colors=['red', 'green', 'blue']))

# Display both plots side by side
fig_voltage.show()
fig_power.show()
