import numpy as np
import pandas as pd
import plotly.graph_objects as go
import sympy as sp

# Given values
power = 25  # in watts
voltage = 120  # in volts

# Calculate resistance using P = V^2 / R
resistance = voltage**2 / power

print("Resistance of the bulb:", resistance)

# Create a dataframe to store temperature and resistance data
data = {'Temperature (°C)': [2700, 2600]}
df = pd.DataFrame(data)

# Define the resistance formula
def resistance_formula(T):
    return resistance * (1 + 0.0045 * (T - 25))

# Calculate resistance values for the given temperatures
df['Resistance at 2600°C'] = df['Temperature (°C)'].apply(resistance_formula)

print(df)

# Create a 3D plot using Plotly
T_vals = np.linspace(2500, 2800, 100)
R_vals = np.linspace(df['Resistance at 2600°C'].min(), df['Resistance at 2600°C'].max(), 100)
T_mesh, R_mesh = np.meshgrid(T_vals, R_vals)

# Calculate resistance values based on the formula for each point on the meshgrid
Z = resistance_formula(T_mesh)

fig = go.Figure(data=[go.Surface(x=T_mesh, y=R_mesh, z=Z)])
fig.update_layout(scene=dict(xaxis_title='Temperature (°C)', yaxis_title='Resistance (Ohms)', zaxis_title='Calculated Resistance'))
fig.show()
