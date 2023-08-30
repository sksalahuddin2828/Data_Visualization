import numpy as np
import pandas as pd
import sympy as sp
import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
voltage_a = 220  # Volts
power_peak_kw = 96.8  # kW
voltage_b = 120  # Volts

# Calculate resistance for 220V AC short circuit
power_peak_w = power_peak_kw * 1000
resistance_a = voltage_a**2 / power_peak_w

# Calculate average power for 120V AC voltage
power_avg_w = voltage_b**2 / resistance_a

# Create a DataFrame for presentation
data = {'Voltage (V)': [voltage_a, voltage_b],
        'Resistance (ohms)': [resistance_a, resistance_a],
        'Power (W)': [power_peak_w, power_avg_w],
        'Type': ['Peak', 'Average']}
df = pd.DataFrame(data)

# Interactive 3D scatter plot using Plotly
fig = px.scatter_3d(df, x='Voltage (V)', y='Resistance (ohms)', z='Power (W)',
                    color='Type', title='Voltage, Resistance, and Power Relationship',
                    labels={'Voltage (V)': 'Voltage (V)', 'Resistance (ohms)': 'Resistance (ohms)', 'Power (W)': 'Power (W)'})

# Add equations as annotations
equation_peak = f'Resistance = {resistance_a:.2f} ohms\nPower = {power_peak_w:.2f} W'
equation_avg = f'Resistance = {resistance_a:.2f} ohms\nPower = {power_avg_w:.2f} W'

fig.update_layout(scene=dict(
    annotations=[
        dict(
            x=voltage_a, y=resistance_a, z=power_peak_w,
            text=equation_peak,
            showarrow=True,
            arrowhead=2,
            ax=30,
            ay=-40
        ),
        dict(
            x=voltage_b, y=resistance_a, z=power_avg_w,
            text=equation_avg,
            showarrow=True,
            arrowhead=2,
            ax=-30,
            ay=-40
        )]
))

# Show the interactive plot
fig.show()

# Additional Mathematical Calculations
time_period = 1 / 60  # Assuming 60 Hz AC frequency
angular_frequency = 2 * np.pi / time_period
current_rms = voltage_a / resistance_a

# Create a time array
time = np.linspace(0, 2 * np.pi, 100)

# Calculate instantaneous current values
current_instantaneous = current_rms * np.sin(angular_frequency * time)

# Create a plot for instantaneous current variation
plt.figure(figsize=(10, 6))
plt.plot(time, current_instantaneous)
plt.xlabel("Time (s)")
plt.ylabel("Instantaneous Current (A)")
plt.title("Instantaneous Current Variation")
plt.grid(True)
plt.show()
