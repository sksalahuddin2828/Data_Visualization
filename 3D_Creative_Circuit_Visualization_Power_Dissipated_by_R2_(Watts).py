# Import the necessary libraries
import numpy as np
import sympy as sp
import plotly.graph_objs as go
import pandas as pd

# Define circuit parameters
V_battery = 12.0  # Battery voltage in volts
R1 = 1.00  # Resistance of R1 in ohms
R2 = 6.00  # Resistance of R2 in ohms
R3 = 13.00  # Resistance of R3 in ohms

# (a) Calculate total resistance
# Create symbolic variables
I_total, I2 = sp.symbols('I_total I2')
# Define equations for current through R1, R2, and R3
eq1 = sp.Eq(I_total, V_battery / (R1 + R2 + R3))
eq2 = sp.Eq(I2, V_battery / (R2 + R3))
# Solve for I_total and I2
solution = sp.solve([eq1, eq2], (I_total, I2))
total_resistance = V_battery / solution[I_total]

# (b) Calculate IR drop in R1
IR_drop_R1 = solution[I_total] * R1

# (c) Find current I2 through R2
current_I2 = solution[I2]

# (d) Calculate power dissipated by R2
power_R2 = current_I2 ** 2 * R2

# Create a 3D visualization of the circuit using Plotly
resistor_data = [
    go.Mesh3d(
        x=[0, R1, R1, 0, 0, R1, R1, 0],
        y=[0, 0, 1, 1, 0, 0, 1, 1],
        z=[0, 0, 0, 0, R1, R1, R1, R1],
        color='red',
        opacity=0.6,
        name='R1'
    ),
    go.Mesh3d(
        x=[R1, R1 + R2, R1 + R2, R1, R1, R1 + R2, R1 + R2, R1],
        y=[0, 0, 1, 1, 0, 0, 1, 1],
        z=[0, 0, 0, 0, R1, R1, R1, R1],
        color='green',
        opacity=0.6,
        name='R2'
    ),
    go.Mesh3d(
        x=[R1 + R2, R1 + R2 + R3, R1 + R2 + R3, R1 + R2, R1 + R2, R1 + R2 + R3, R1 + R2 + R3, R1 + R2],
        y=[0, 0, 1, 1, 0, 0, 1, 1],
        z=[0, 0, 0, 0, R1, R1, R1, R1],
        color='blue',
        opacity=0.6,
        name='R3'
    )
]

layout = go.Layout(
    scene=dict(
        xaxis=dict(title='X'),
        yaxis=dict(title='Y'),
        zaxis=dict(title='Resistance (Ohms)')
    ),
    title='Circuit Visualization'
)

fig = go.Figure(data=resistor_data, layout=layout)

# Display the interactive 3D plot using Plotly
fig.show()

# Create a Pandas DataFrame for results
results_df = pd.DataFrame({
    'Parameter': ['Total Resistance (Ohms)', 'IR Drop in R1 (Volts)', 'Current I2 (Amps)', 'Power Dissipated by R2 (Watts)'],
    'Value': [total_resistance, IR_drop_R1, current_I2, power_R2]
})

# Display the results using Pandas
print(results_df)
