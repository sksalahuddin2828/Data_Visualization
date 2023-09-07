import numpy as np
import pandas as pd
import sympy as sp
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Given data
galvanometer_sensitivity = 50e-6  # in Amperes
galvanometer_resistance = 25.0  # in Ohms
full_scale_voltage = 3000.0  # in Volts

# Create a function to calculate the unknown resistance
def calculate_unknown_resistance(sensitivity, voltage):
    current_galvanometer = voltage / galvanometer_resistance
    return (voltage / current_galvanometer) - galvanometer_resistance

# Create a grid of sensitivity and voltage values
sensitivity_values = np.linspace(1e-6, 100e-6, 100)
voltage_values = np.linspace(1, 10000, 100)
sensitivity_grid, voltage_grid = np.meshgrid(sensitivity_values, voltage_values)
resistance_grid = np.vectorize(calculate_unknown_resistance)(sensitivity_grid, voltage_grid)

# Create a pandas DataFrame for the grid
df = pd.DataFrame({
    'Sensitivity (A/V)': sensitivity_grid.ravel(),
    'Full-Scale Voltage (V)': voltage_grid.ravel(),
    'Unknown Resistance (Ohms)': resistance_grid.ravel()
})

# Create interactive 3D scatter plot using Plotly
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
scatter = go.Scatter3d(
    x=df['Sensitivity (A/V)'],
    y=df['Full-Scale Voltage (V)'],
    z=df['Unknown Resistance (Ohms)'],
    mode='markers',
    marker=dict(size=4),
    text='Unknown Resistance (Ohms)',
    opacity=0.7,
)
fig.add_trace(scatter)
fig.update_layout(
    scene=dict(
        xaxis_title='Sensitivity (A/V)',
        yaxis_title='Full-Scale Voltage (V)',
        zaxis_title='Unknown Resistance (Ohms)',
    ),
    title='Interactive 3D Visualization of Unknown Resistance',
)

# Show the interactive plot in a Jupyter Notebook
fig.show()
