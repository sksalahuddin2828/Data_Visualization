import numpy as np
import pandas as pd
import plotly.graph_objs as go

# Given data
power = 1.44e3  # in watts
resistance = 0.100  # in ohms

# Calculate current using P = I^2 * R
current = np.sqrt(power / resistance)

# Calculate voltage using Ohm's Law: V = I * R
voltage = current * resistance

# Create a range of current and resistance values
current_range = np.linspace(0.01, 10, 100)
resistance_range = np.linspace(0.01, 2, 100)
current_range, resistance_range = np.meshgrid(current_range, resistance_range)
voltage_range = current_range * resistance_range

# Create an interactive 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(z=voltage_range, x=current_range, y=resistance_range)])
fig.update_layout(
    title='Voltage as a Function of Current and Resistance',
    scene=dict(xaxis_title='Current (A)', yaxis_title='Resistance (Ω)', zaxis_title='Voltage (V)')
)
fig.show()

# Create a Pandas DataFrame to showcase the data
data = {'Current (A)': current_range.flatten(), 'Resistance (Ω)': resistance_range.flatten(), 'Voltage (V)': voltage_range.flatten()}
df = pd.DataFrame(data)
print(df)
