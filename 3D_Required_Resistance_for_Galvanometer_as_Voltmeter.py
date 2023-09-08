import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Constants
galvanometer_sensitivity = 100e-6  # 100 μA
galvanometer_resistance = 10.0  # 10.0 Ω

# (a) Full-scale reading of 300 V
full_scale_reading_a = 300.0  # 300 V

# Calculate resistance needed for (a)
def calculate_resistance_a(full_scale_voltage_a):
    resistance_a = (full_scale_voltage_a / galvanometer_sensitivity) - galvanometer_resistance
    return resistance_a

resistance_a = calculate_resistance_a(full_scale_reading_a)

# (b) Full-scale reading of 0.300 V
full_scale_reading_b = 0.300  # 0.300 V

# Calculate resistance needed for (b)
def calculate_resistance_b(full_scale_voltage_b):
    resistance_b = (full_scale_voltage_b / galvanometer_sensitivity) - galvanometer_resistance
    return resistance_b

resistance_b = calculate_resistance_b(full_scale_reading_b)

# Create a Pandas DataFrame for the results
data = {'Voltage (V)': [full_scale_reading_a, full_scale_reading_b],
        'Required Resistance (Ω)': [resistance_a, resistance_b]}
df = pd.DataFrame(data, index=['Scenario (a)', 'Scenario (b)'])

# Data Visualization using Plotly
fig = px.bar(df, x=df.index, y='Required Resistance (Ω)', title='Required Resistance for Galvanometer as Voltmeter')
fig.update_traces(marker_color='blue')

# Print the results
print(df)

# Show the Plotly visualization
fig.show()
