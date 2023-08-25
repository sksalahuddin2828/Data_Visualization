import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

# Parameters
V0 = 10  # Peak voltage
R = 5    # Resistance

# Frequency range
freq_range = np.linspace(10, 1000, 50)  # Frequencies to visualize

# Calculate phase difference and impedance
phase_diffs = []
impedances = []

for f in freq_range:
    V = V0 * np.sin(2 * np.pi * f * t)
    I = V / R
    phase_diff = np.arctan2(I, V)  # Phase difference calculation
    impedance = V0 / (R + 1j * (2 * np.pi * f) * R)  # Impedance calculation
    phase_diffs.append(phase_diff.mean())  # Taking average phase difference
    impedances.append(np.abs(impedance))  # Impedance magnitude

# Create a DataFrame for the impedance and phase difference data
impedance_df = pd.DataFrame({'Frequency': freq_range, 'Impedance': impedances, 'Phase Difference': phase_diffs})

# Custom 3D Scatter Plot
fig = px.scatter_3d(impedance_df, x='Frequency', y='Phase Difference', z='Impedance', 
                    title='Frequency vs. Phase Difference vs. Impedance',
                    labels={'Frequency': 'Frequency (Hz)', 'Phase Difference': 'Phase Difference (radians)', 'Impedance': 'Impedance'},
                    color='Impedance', size='Impedance', opacity=0.8)

# Customizing the marker colorscale
fig.update_traces(marker=dict(showscale=True, colorscale='Viridis'))

# Show the 3D Scatter Plot
fig.show()
