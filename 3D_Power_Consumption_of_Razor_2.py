import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given data
voltage = 240  # Voltage in volts
power_north_america = 25.0  # Power in watts

# Calculate resistance using P = V^2 / R
resistance = (voltage ** 2) / power_north_america

# Create a range of resistance values for visualization
resistance_values = np.linspace(1, 100, 100)
voltage_values = np.sqrt(power_north_america * resistance_values)

# Calculate power consumption for each resistance value
power_consumption = (voltage_values ** 2) / resistance_values

# Create a DataFrame for easy manipulation
data = pd.DataFrame({'Resistance': resistance_values, 'Voltage': voltage_values, 'Power': power_consumption})

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(z=data['Power'].values.reshape(100, -1), x=data['Resistance'], y=data['Voltage'])])
fig.update_layout(title='Power Consumption of Razor',
                  scene=dict(xaxis_title='Resistance', yaxis_title='Voltage', zaxis_title='Power'))

# Add scatter plot to show the selected resistance and power point
selected_resistance = 50
selected_power = (voltage ** 2) / selected_resistance
fig.add_trace(go.Scatter3d(x=[selected_resistance], y=[np.sqrt(power_north_america * selected_resistance)], z=[selected_power],
                           mode='markers', marker=dict(size=8, color='red'), name='Selected Point'))

# Show the interactive plot
fig.show()
