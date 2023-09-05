import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given data
emf = 12.0  # V
terminal_voltage = 15.0  # V
current = 8.00  # A

# Calculate internal resistance (R)
R = (emf - terminal_voltage) / current

# Display the internal resistance
print(f"Internal Resistance (R): {R:.2f} ohms")

# Create a grid of values for emf and terminal voltage
emf_values = np.linspace(0, 20, 100)
terminal_voltage_values = np.linspace(0, 20, 100)
emf_values, terminal_voltage_values = np.meshgrid(emf_values, terminal_voltage_values)

# Calculate internal resistance for each combination of emf and terminal voltage
current_values = (emf_values - terminal_voltage_values) / R

# Create a Pandas DataFrame for the data
df = pd.DataFrame({
    'EMF (V)': emf_values.flatten(),
    'Terminal Voltage (V)': terminal_voltage_values.flatten(),
    'Current (A)': current_values.flatten()
})

# Create an interactive 3D scatter plot using Plotly
scatter_plot = px.scatter_3d(df, x='EMF (V)', y='Terminal Voltage (V)', z='Current (A)',
                              title='Current vs EMF and Terminal Voltage',
                              labels={'EMF (V)': 'EMF', 'Terminal Voltage (V)': 'Terminal Voltage', 'Current (A)': 'Current'},
                              color='Current (A)',
                              color_continuous_scale='Viridis')

# Add a surface plot to show the calculated current values
surface_plot = go.Surface(x=emf_values, y=terminal_voltage_values, z=current_values,
                          colorscale='Viridis', showscale=False)

scatter_plot.add_trace(surface_plot)

# Create a dynamic table using Plotly
table = go.Figure(data=[go.Table(
    header=dict(values=["EMF (V)", "Terminal Voltage (V)", "Current (A)"]),
    cells=dict(values=[df['EMF (V)'], df['Terminal Voltage (V)'], df['Current (A)']])
)])

table.update_layout(title='Data Table')

# Show the interactive scatter plot and table
scatter_plot.show()
table.show()
