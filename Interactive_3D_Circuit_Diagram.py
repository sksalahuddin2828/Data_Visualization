import numpy as np
import sympy as sp
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# Constants
R_g = 25.0  # Galvanometer resistance in ohms
I_g = 50e-6  # Galvanometer sensitivity in A
I_full = 10.0  # Full-scale current in A

# Calculate shunt resistance
R_s = R_g / (I_full / I_g - 1)

# Create a Pandas DataFrame for data visualization
data = {'Shunt Resistance (R_s) [Ω]': [], 'Full-scale Current (I_full) [A]': [], 'Galvanometer Current (I_g) [A]': []}
for R_s_val in np.linspace(0, 50, 100):  # Adjust the range as needed
    for I_full_val in np.linspace(1, 20, 100):  # Adjust the range as needed
        I_g_calculated = R_g / (R_s_val + R_g) * I_full_val
        data['Shunt Resistance (R_s) [Ω]'].append(R_s_val)
        data['Full-scale Current (I_full) [A]'].append(I_full_val)
        data['Galvanometer Current (I_g) [A]'].append(I_g_calculated)

df = pd.DataFrame(data)

# Create an interactive 3D scatter plot using Plotly Express
fig = px.scatter_3d(df, x='Shunt Resistance (R_s) [Ω]', y='Full-scale Current (I_full) [A]',
                    z='Galvanometer Current (I_g) [A]', color='Galvanometer Current (I_g) [A]')
fig.update_layout(scene=dict(xaxis_title='Shunt Resistance (R_s) [Ω]',
                             yaxis_title='Full-scale Current (I_full) [A]',
                             zaxis_title='Galvanometer Current (I_g) [A]'))
fig.update_traces(marker=dict(size=3))
fig.update_layout(title='Interactive 3D Plot Using Plotly')
fig.show()
