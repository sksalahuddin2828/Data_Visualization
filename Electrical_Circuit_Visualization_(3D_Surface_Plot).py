import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Constants
cell_voltage = 3.0000  # V
load_current = 0.300  # mA
internal_resistance = 2.00  # Ohms

# Calculate the equivalent resistance of the circuit
equivalent_resistance = internal_resistance

# Create a range of values for equivalent resistance and load current
resistance_range = np.linspace(0, equivalent_resistance, 100)
current_range = np.linspace(0, load_current / 1000, 100)  # Convert mA to A

# Create a grid of equivalent resistance and load current values
R, I = np.meshgrid(resistance_range, current_range)

# Calculate voltage drop and output voltage over the grid
voltage_drop = R * I
output_voltage = cell_voltage - voltage_drop

# Create a Pandas DataFrame to display the results in a table
df = pd.DataFrame({'Equivalent Resistance (Ohms)': R.flatten(),
                   'Load Current (A)': I.flatten(),
                   'Output Voltage (V)': output_voltage.flatten()})

# Display the table
print(df)

# Create an interactive 3D surface plot using Plotly
fig = go.Figure(data=[go.Surface(z=output_voltage, x=R, y=I)])
fig.update_layout(scene=dict(xaxis_title='Equivalent Resistance (Ohms)',
                             yaxis_title='Load Current (A)',
                             zaxis_title='Output Voltage (V)'),
                  title='Electrical Circuit Visualization (3D Surface Plot)')

# Show the interactive plot
fig.show()
