import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sympy as sp

# Constants
mass_oxygen_ion = 2.66e-26  # kg
velocity = 5.00e6  # m/s
magnetic_field = 1.20  # T
radius = 0.231  # m
electron_charge = 1.602e-19  # C

# Calculate charge of the oxygen-16 ion
charge = (mass_oxygen_ion * velocity) / (radius * magnetic_field)

# Calculate the ratio of charge to electron charge
charge_ratio = charge / electron_charge

# Calculate radius for an electron
# Rearrange the formula: r = (m * v) / (q * B)
radius_electron = (mass_oxygen_ion * velocity) / (electron_charge * magnetic_field)

# Create a DataFrame to store the results
data = {
    'Particle': ['Oxygen-16 Ion', 'Electron'],
    'Charge (C)': [charge, electron_charge]
}
result_df = pd.DataFrame(data)

# Visualization
# Create an interactive bar chart using Plotly Express
charge_chart = px.bar(result_df, x='Particle', y='Charge (C)',
                      title='Charge Comparison: Oxygen-16 Ion vs. Electron',
                      labels={'Charge (C)': 'Charge (Coulombs)'})
charge_chart.update_traces(marker_color=['blue', 'red'])

# Create an interactive 3D plot of the circular path of the ion using Plotly
theta = np.linspace(0, 2 * np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.zeros_like(theta)

ion_path_3d = go.Scatter3d(x=x, y=y, z=z, mode='lines',
                           marker=dict(size=4, color='blue'),
                           name='Circular Path')
layout = go.Layout(scene=dict(aspectmode="cube"))
ion_path_fig = go.Figure(data=[ion_path_3d], layout=layout)
ion_path_fig.update_layout(title='Circular Path of Oxygen-16 Ion',
                           scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Display the results using Plotly
charge_chart.show()
ion_path_fig.show()

# Print the calculated results
print(f"(a) Charge of the oxygen-16 ion: {charge} C")
print(f"(b) Charge ratio to an electron: {charge_ratio}")
print(f"(c) Radius of circular path for an electron: {radius_electron} m")

# Add explanations, annotations, and text labels to the plots to make them more informative and creative.
