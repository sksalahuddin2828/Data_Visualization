import numpy as np
import pandas as pd
import plotly.express as px

# Create DataFrame for Phasor diagram
phasor_data = {'Impedance': [np.complex(220, 0) + 2j*np.complex(np.cos(np.pi/6), np.sin(np.pi/6))]}
phasor_df = pd.DataFrame(phasor_data)

# Convert complex numbers to magnitudes and angles for polar plot
phasor_df['Magnitude'] = np.abs(phasor_df['Impedance'])
phasor_df['Angle'] = np.angle(phasor_df['Impedance'], deg=True)

# Interactive Polar Phasor diagram using Plotly
fig_phasor = px.scatter_polar(phasor_df, r='Magnitude', theta='Angle', title='Interactive Phasor Diagram')
fig_phasor.update_traces(marker=dict(size=10))
fig_phasor.show()
