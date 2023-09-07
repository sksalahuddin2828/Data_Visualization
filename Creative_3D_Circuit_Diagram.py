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

# Determine the dimensions of the DataFrame
num_rows = len(df['Shunt Resistance (R_s) [Ω]'].unique())
num_cols = len(df['Full-scale Current (I_full) [A]'].unique())

# Create an interactive 3D surface plot using Plotly
fig = go.Figure()

# Create the surface plot
fig.add_trace(go.Surface(
    z=df['Galvanometer Current (I_g) [A]'].values.reshape(num_rows, num_cols),
    x=df['Shunt Resistance (R_s) [Ω]'].values.reshape(num_rows, num_cols),
    y=df['Full-scale Current (I_full) [A]'].values.reshape(num_rows, num_cols),
    colorscale='Viridis',
    colorbar=dict(title='Galvanometer Current (I_g) [A]')
))

# Add annotations and labels
fig.update_layout(
    scene=dict(
        xaxis_title='Shunt Resistance (R_s) [Ω]',
        yaxis_title='Full-scale Current (I_full) [A]',
        zaxis_title='Galvanometer Current (I_g) [A]',
    ),
    title='Interactive 3D Surface Plot Using Plotly',
)

# Show the interactive plot
fig.show()
