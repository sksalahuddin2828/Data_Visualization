import plotly.graph_objs as go
import numpy as np

galvanometer_resistance = 40.0  # Ω
sensitivity = 25.0e-6  # A
full_scale_voltage = 0.500e-3  # V

# Generate data points
sensitivity_range = np.linspace(1e-6, 50e-6, 100)
full_scale_voltage_range = np.linspace(1e-3, 1, 100)
sensitivity_mesh, full_scale_voltage_mesh = np.meshgrid(sensitivity_range, full_scale_voltage_range)

# Calculate required resistance for each combination
required_resistance_mesh = full_scale_voltage_mesh / sensitivity_mesh - galvanometer_resistance


# Create a 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(z=required_resistance_mesh, x=sensitivity_range, y=full_scale_voltage_range)])
fig.update_layout(scene=dict(xaxis_title='Sensitivity (A)', yaxis_title='Full-scale Voltage (V)', zaxis_title='Required Resistance (Ω)'),
                  title='Required Resistance for Galvanometer to be Used as a Voltmeter')
fig.show()

import pandas as pd

# Create a dataframe to store the sensitivity, full-scale voltage, and required resistance data
data = {'Sensitivity (A)': sensitivity_mesh.flatten(),
        'Full-scale Voltage (V)': full_scale_voltage_mesh.flatten(),
        'Required Resistance (Ω)': required_resistance_mesh.flatten()}
df = pd.DataFrame(data)

# Display the first few rows of the dataframe
print(df.head())
