import sympy as sp
import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Define symbolic variables
I1, I2, I3 = sp.symbols('I1 I2 I3')

# Define circuit parameters
emf1 = 18  # emf1 value
emf2 = 45  # emf2 value
R1 = 6     # R1 value
R2 = 3     # R2 value
R3 = 2     # R3 value
r1 = 6     # r1 value
r2 = 2     # r2 value

# Define equations from Kirchhoff's rules
eq1 = sp.Eq(I1, I2 + I3)
eq2 = sp.Eq(-I2 * (R2 + r1) + emf1 - I1 * R1, 0)
eq3 = sp.Eq(I1 * R1 + I3 * (R3 + r2) - emf2, 0)

# Solve the system of equations
solution = sp.solve((eq1, eq2, eq3), (I1, I2, I3))

# Extract numerical values as floats
I1_val = float(solution[I1])
I2_val = float(solution[I2])
I3_val = float(solution[I3])

# Create a Pandas DataFrame for results
data = {'Branch': ['I1', 'I2', 'I3'],
        'Current (A)': [I1_val, I2_val, I3_val]}
currents_df = pd.DataFrame(data)

# Create a 3D scatter plot using Plotly
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
fig.add_trace(go.Scatter3d(x=[I1_val], y=[I3_val], z=[I2_val],
                           mode='markers', marker=dict(size=10, color='blue'),
                           text=['Equilibrium Point']))

# Add labels and title
fig.update_layout(scene=dict(xaxis_title='I1 (A)', yaxis_title='I3 (A)', zaxis_title='I2 (A)'),
                  title='Currents in the Circuit')

# Show the 3D plot
fig.show()

# Display the numerical results
print(currents_df)
