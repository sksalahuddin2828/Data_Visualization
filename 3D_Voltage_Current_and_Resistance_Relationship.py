import numpy as np
import pandas as pd
import sympy as sp
import torch
import matplotlib.pyplot as plt
import plotly.express as px

# Define the given values
V1 = 120  # Voltage for the first device (in volts)
V2 = 240  # Voltage for the second device (in volts)
P = 1000  # Power consumption for both devices (in watts)

# Calculate resistance ratios
R1 = V1**2 / P
R2 = V2**2 / P
resistance_ratio = R2 / R1

# Calculate current ratios
I1 = V1 / R1
I2 = V2 / R2
current_ratio = I2 / I1

# Calculate power increase factor
power_increase_factor = (V2 / V1)**2

# Create a 3D visualization
voltage_range = np.linspace(0, 300, 100)
current_range = np.linspace(0, 10, 100)
voltage_grid, current_grid = np.meshgrid(voltage_range, current_range)
resistance_grid = voltage_grid / current_grid

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(voltage_grid, current_grid, resistance_grid, cmap='viridis')
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Resistance (Ω)')
ax.set_title('Voltage, Current, and Resistance Relationship')
plt.show()

# Create interactive data visualizations using Plotly
data = {'Voltage': [V1, V2], 'Current': [I1, I2]}
df = pd.DataFrame(data, index=['Device 1', 'Device 2'])
fig = px.bar(df, x=df.index, y='Current', title='Current Consumption Comparison')
fig.update_layout(xaxis_title='Device', yaxis_title='Current (A)')
fig.show()

# Print the results
print(f"Resistance Ratio: {resistance_ratio:.2f}")
print(f"Current Ratio: {current_ratio:.2f}")
print(f"Power Increase Factor: {power_increase_factor:.2f}")
