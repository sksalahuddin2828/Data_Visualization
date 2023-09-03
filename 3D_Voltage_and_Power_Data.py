import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Define resistances
resistors = {'R1': 2, 'R2': 3, 'R3': 4}

# Calculate total resistance
total_resistance = sum(resistors.values())

# Generate current values
current_values = np.linspace(0.1, 5, 100)

# Calculate voltage and power for each resistor
data = {'Current (I)': current_values}
for resistor, resistance in resistors.items():
    data[f'Voltage ({resistor})'] = current_values * resistance
    data[f'Power ({resistor})'] = (current_values ** 2) * resistance

# Create a DataFrame
df = pd.DataFrame(data)

# Create interactive 3D plot using Plotly
fig = go.Figure(data=[
    go.Scatter3d(x=df['Current (I)'], y=df['Current (I)'] * resistors['R1'], z=df['Voltage (R1)'], mode='lines', name='R1'),
    go.Scatter3d(x=df['Current (I)'], y=df['Current (I)'] * resistors['R2'], z=df['Voltage (R2)'], mode='lines', name='R2'),
    go.Scatter3d(x=df['Current (I)'], y=df['Current (I)'] * resistors['R3'], z=df['Voltage (R3)'], mode='lines', name='R3'),
])
fig.update_layout(scene=dict(xaxis_title='Current (I)', yaxis_title='Power (P)', zaxis_title='Voltage (V)'))

# Create an interactive table using Plotly
table = go.Figure(data=[go.Table(
    header=dict(values=list(df.columns)),
    cells=dict(values=[df[col] for col in df.columns]))
])
table.update_layout(title='Voltage and Power Data')

# Display the figures using Plotly
fig.show()
table.show()
