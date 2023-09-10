import numpy as np
import pandas as pd
import plotly.express as px

# Given data
emf_standard = 3.0  # Standard EMF in volts
rs_values = np.linspace(10.0, 20.0, 50)  # Range of Rs values from 10.0 Ω to 20.0 Ω
emfx_values = np.linspace(0.0, 5.0, 50)  # Range of unknown EMF values from 0.0 V to 5.0 V

# Create a grid of Rs and EMFx values
rs_grid, emfx_grid = np.meshgrid(rs_values, emfx_values)

# Calculate corresponding Rx values using the potentiometer formula
rx_grid = emfx_grid * (rs_grid / emf_standard - 1)

# Create a Pandas DataFrame for the data
data = pd.DataFrame({'Rs': rs_grid.ravel(), 'EMFx': emfx_grid.ravel(), 'Rx': rx_grid.ravel()})

# Use Plotly to create an interactive 3D surface plot
fig = px.scatter_3d(data, x='Rs', y='EMFx', z='Rx', color='Rx',
                    title='3D Visualization of Potentiometer Balance',
                    labels={'Rx': 'Rx (Ω)'})
fig.update_traces(marker=dict(size=2))
fig.update_layout(scene=dict(xaxis_title='Rs (Ω)', yaxis_title='EMFx (V)', zaxis_title='Rx (Ω)'))

# Show the interactive plot in a web browser
fig.show()

# Now, let's find the Rx value for emfx = 3.1 V and Rs = 15.0 Ω
target_emfx = 3.1
target_rs = 15.0

# Interpolate the Rx value
from scipy.interpolate import griddata
target_rx = griddata((rs_grid.ravel(), emfx_grid.ravel()), rx_grid.ravel(), (target_rs, target_emfx), method='linear')

print(f"For EMFx = {target_emfx} V and Rs = {target_rs} Ω, Rx = {target_rx:.2f} Ω")
