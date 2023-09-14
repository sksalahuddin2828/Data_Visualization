import numpy as np
import plotly.express as px
import pandas as pd

# Given data
B = 0.200  # Magnetic field strength in Tesla
diameter_aorta = 0.026  # Diameter of aorta in meters
velocity_blood = 0.6  # Blood velocity in m/s

# Calculate the Hall voltage
hall_voltage = B * diameter_aorta * velocity_blood

# Create a Pandas DataFrame for visualization
data = {'Parameter': ['Magnetic Field (B)', 'Diameter (d)', 'Velocity (v)', 'Hall Voltage'],
        'Value': [B, diameter_aorta, velocity_blood, hall_voltage]}

df = pd.DataFrame(data)

# Create a sunburst chart to visualize the data
fig = px.sunburst(df, path=['Parameter'], values='Value', color='Value',
                  color_continuous_scale='RdBu', title="Hall Voltage in a Blood Vessel")

fig.show()
