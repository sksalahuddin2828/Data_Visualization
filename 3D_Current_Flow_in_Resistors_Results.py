import numpy as np
import sympy as sp
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots
from IPython.display import display

# Define the given values
V = 12.0  # Voltage output of the battery (in volts)
R1 = 1.00  # Resistance of R1 (in ohms)
R2 = 6.00  # Resistance of R2 (in ohms)
R3 = 13.0  # Resistance of R3 (in ohms)

# (a) Calculate total resistance (Rp) for the parallel connection
Rp_inv = 1 / R1 + 1 / R2 + 1 / R3
Rp = 1 / Rp_inv
Rp = round(Rp, 3)  # Round to three decimal places

# (b) Calculate total current (I)
I = V / Rp

# (c) Calculate currents in each resistor
I1 = V / R1
I2 = V / R2
I3 = V / R3

# (d) Calculate power dissipated by each resistor
P1 = I1 ** 2 * R1
P2 = I2 ** 2 * R2
P3 = I3 ** 2 * R3

# (e) Calculate power output of the source
P_source = V * I

# Create a table to display the results using Pandas
data = {
    'Component': ['Total Resistance (Rp)', 'Total Current (I)', 'R1 Current (I1)', 'R2 Current (I2)', 'R3 Current (I3)',
                  'R1 Power (P1)', 'R2 Power (P2)', 'R3 Power (P3)', 'Power Source (P_source)'],
    'Value': [Rp, I, I1, I2, I3, P1, P2, P3, P_source]
}
results_df = pd.DataFrame(data)

# Display the table using Pandas
display(results_df)

# Create a 3D interactive plot using Plotly
resistor_labels = ['R1', 'R2', 'R3']
current_magnitudes = [I1, I2, I3]

trace3d = []
for i, label in enumerate(resistor_labels):
    trace3d.append(go.Mesh3d(x=[0], y=[i], z=[0], text=[f'{label} I={current_magnitudes[i]:.2f}A'],
                             hoverinfo='text', opacity=0.5))

layout = go.Layout(scene=dict(aspectmode="cube"))
fig3d = go.Figure(data=trace3d, layout=layout)
fig3d.update_layout(title="Current Flow in Resistors",
                    scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Current (A)"))

# You can display the Plotly figure interactively or save it as an HTML file.
fig3d.show()
fig3d.write_html("parallel_circuit_results.html")
