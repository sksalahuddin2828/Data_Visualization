import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Create data points for the plot
current_values = np.linspace(100, 1000, 10)
voltage_values = np.linspace(100, 1000, 10)
current_values, voltage_values = np.meshgrid(current_values, voltage_values)
power_loss = (current_values**2 * R) / (current_values * voltage_values)

# Create a 3D surface plot
fig = go.Figure(data=[go.Surface(z=power_loss, x=current_values, y=voltage_values)])
fig.update_layout(scene=dict(xaxis_title='Current (A)', yaxis_title='Voltage (V)', zaxis_title='Power Loss (W)'),
                  title='Power Loss in Transmission Lines')

# Show the plot
fig.show()
