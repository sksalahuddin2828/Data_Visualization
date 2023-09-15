import numpy as np
import plotly.graph_objects as go

# Given data
calibrated_voltage = 1.00e-6  # 1.00 μV
calibrated_field = 2.00  # 2.00-T
new_field = 0.150  # 0.150-T

# Calculate the Hall coefficient
hall_coefficient = calibrated_voltage / calibrated_field

# Calculate the output voltage in the new field
output_voltage = hall_coefficient * new_field

# Create a gauge chart to represent the output voltage
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=output_voltage,
    title="Output Voltage (V)",
    gauge={'axis': {'range': [None, output_voltage * 1.2]}}
))

fig.show()

import numpy as np
import plotly.express as px

# Given data
magnetic_field = 2.00  # 2.00-T
wire_diameter_mm = 2.588  # 10-gauge copper wire diameter in mm
current = 20.0  # 20.0 A

# Convert wire diameter to meters
wire_diameter_m = wire_diameter_mm / 1000

# Calculate the Hall voltage using the formula for Hall coefficient
hall_coefficient_copper = 5.8e-11  # Assuming a Hall coefficient for copper
hall_voltage = hall_coefficient_copper * magnetic_field * current / (np.pi * (wire_diameter_m / 2)**2)

# Create a bar chart to display the Hall voltage
data = {'Wire Diameter (mm)': [wire_diameter_mm], 'Hall Voltage (V)': [hall_voltage]}
df = pd.DataFrame(data)

fig = px.bar(df, x='Wire Diameter (mm)', y='Hall Voltage (V)', title='Hall Voltage vs. Wire Diameter')
fig.show()

import numpy as np
import plotly.graph_objects as go

# Given data
magnetic_field = 2.00  # 2.00-T
current = 20.0  # 20.0 A

# Create an array of wire diameters (e.g., from 1 mm to 10 mm)
wire_diameters_mm = np.linspace(1, 10, 100)
wire_diameters_m = wire_diameters_mm / 1000

# Calculate the Hall voltages for each wire diameter
hall_voltages = hall_coefficient_copper * magnetic_field * current / (np.pi * (wire_diameters_m / 2)**2)

# Create a scatter plot to show the inverse proportionality
fig = go.Figure()
fig.add_trace(go.Scatter(x=1/wire_diameters_mm, y=hall_voltages, mode='markers', name='Hall Voltage vs. 1/Diameter'))
fig.update_xaxes(title='1/Wire Diameter (1/mm)')
fig.update_yaxes(title='Hall Voltage (V)')
fig.update_layout(title='Inverse Proportionality: Hall Voltage vs. 1/Diameter')
fig.show()
