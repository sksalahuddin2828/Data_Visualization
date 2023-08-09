import numpy as np
import pandas as pd
import plotly.graph_objs as go
from sympy import symbols, Eq, solve

# Define constants and variables
mu = 0.03  # Linear density in kg/m
length = 2.0  # Length of the string in meters
tension_values = np.linspace(10, 40, 100)  # Tension values in N

# Calculate wave speeds and frequencies
wave_speeds = np.sqrt(tension_values / mu)
frequencies = wave_speeds / length

# Create Pandas DataFrame
results_df = pd.DataFrame({'Tension (N)': tension_values, 'Wave Speed (m/s)': wave_speeds, 'Frequency (Hz)': frequencies})

# Display DataFrame
print(results_df)

# Create 3D Visualization using Plotly
fig = go.Figure(data=[go.Scatter3d(x=tension_values, y=wave_speeds, z=frequencies, mode='markers')])
fig.update_layout(scene=dict(xaxis_title='Tension (N)', yaxis_title='Wave Speed (m/s)', zaxis_title='Frequency (Hz)'),
                  title='Frequency vs. Tension and Wave Speed', margin=dict(l=0, r=0, b=0, t=40))

# Show 3D Visualization
fig.show()
