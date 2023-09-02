import numpy as np
import plotly.graph_objects as go

# Define the values
R1 = 1.00  # Ohms
R2 = 2.00  # Ohms
R3 = 3.00  # Ohms
V_total = 12.0  # Volts

# Calculate total resistance
R_total = 1 / (1/R1 + 1/R2 + 1/R3)

# Calculate total current using Ohm's law
I_total = V_total / R_total

# Calculate IR drop in R1
V1 = I_total * R1

# Create a 3D surface plot
x = [0, 0, 0, 0]
y = [0, 0, 0, 1]
z = [0, V_total, 0, 0]

resistor_labels = ['Total Resistance', 'R1', 'R2', 'R3']
resistor_values = [R_total, R1, R2, R3]

fig = go.Figure()

# Add 3D scatter points for resistor icons
fig.add_trace(go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers+text',
    text=resistor_labels,
    textposition='top center',
    hoverinfo='text',
    marker=dict(size=10, symbol='square'),
))

# Customize the layout
fig.update_layout(
    scene=dict(
        xaxis_title='X',
        yaxis_title='Y',
        zaxis_title='Voltage (V)',
    ),
    title='Creative 3D Visualization of Resistors in Combination',
)

# Show the interactive Plotly figure
fig.show()
