import plotly.graph_objects as go

# Given data
B = 0.200  # Magnetic field strength in Tesla
diameter_aorta = 0.026  # Diameter of aorta in meters
velocity_blood = 0.6  # Blood velocity in m/s

# Calculate the Hall voltage
hall_voltage = B * diameter_aorta * velocity_blood

# Create an interactive gauge chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=hall_voltage,
    title={'text': "Hall Voltage"},
    gauge={'axis': {'range': [None, hall_voltage * 2]},
           'steps': [
               {'range': [0, hall_voltage], 'color': "lightgray"},
               {'range': [hall_voltage, hall_voltage * 2], 'color': "gray"}],
           'threshold': {
               'line': {'color': "red", 'width': 4},
               'thickness': 0.75, 'value': hall_voltage}}))

fig.show()
