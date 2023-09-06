import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

battery_voltage = 12.0  # V
internal_resistance_battery = 0.0100  # Ω
starter_motor_resistance = 0.0500  # Ω
corroded_resistance = 0.0900  # Ω

total_resistance = internal_resistance_battery + starter_motor_resistance
current = battery_voltage / total_resistance
print(f"Current to the motor: {current:.4f} A")

voltage_applied = current * starter_motor_resistance
print(f"Voltage applied to the motor: {voltage_applied:.4f} V")

power = current * voltage_applied
print(f"Power supplied to the motor: {power:.4f} W")

# Create a range of corroded resistances
corroded_resistances = np.linspace(0.0100, 0.1000, 100)

# Calculate current, voltage, and power for each corroded resistance
currents = battery_voltage / (internal_resistance_battery + corroded_resistances)
voltages = currents * starter_motor_resistance
powers = currents * voltages

# Create a Pandas DataFrame
data = pd.DataFrame({'Corroded Resistance (Ω)': corroded_resistances,
                     'Current (A)': currents,
                     'Power (W)': powers})

# Create an interactive line plot using Plotly Express
fig = px.line(data, x='Corroded Resistance (Ω)', y=['Current (A)', 'Power (W)'],
              title='Current and Power vs. Corroded Resistance')
fig.update_xaxes(title_text='Corroded Resistance (Ω)')
fig.update_yaxes(title_text='Value')
fig.show()
