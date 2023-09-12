# Import necessary libraries
import numpy as np
import sympy as sp
import pandas as pd
import plotly.graph_objs as go
from IPython.display import HTML, display, Math

# Define constants
velocity = 4.00e3  # m/s
magnetic_field_strength = 1.25  # T
magnetic_force = 1.40e-16  # N
electron_charge = -1.602e-19  # C (charge of an electron)

# Calculate the angle using sympy
angle_symbolic = sp.asin(magnetic_force / (electron_charge * velocity * magnetic_field_strength))

# Convert the angle to degrees
angle_degrees = sp.deg(angle_symbolic).evalf()

# Create a time range for the motion (adjust as needed)
time_range = np.linspace(0, 1e-7, 1000)

# Calculate the trajectory
x = velocity * time_range
y = np.zeros_like(x)  # Initialize y as an array of zeros
z = np.zeros_like(x)  # Initialize z as an array of zeros

# Create a pandas DataFrame to store data
data = pd.DataFrame({'Time (s)': time_range, 'X Position (m)': x})

# Create a 3D scatter plot using Plotly
scatter = go.Scatter3d(x=x, y=y, z=z, mode='lines', name='Electron Path')
fig_3d = go.Figure(data=[scatter])
fig_3d.update_layout(scene=dict(xaxis_title='X-axis', yaxis_title='Y-axis', zaxis_title='Z-axis'))
fig_3d.update_layout(title_text='Electron Motion in Magnetic Field')

# Create an interactive table with pandas DataFrame
table = go.Figure(data=[go.Table(header=dict(values=list(data.columns)),
                 cells=dict(values=[data['Time (s)'], data['X Position (m)']]))
                     ])
table.update_layout(title='Electron Motion Data Table')

# Explanation and Theory
theory_text = f"""
### Electron Motion in a Magnetic Field

When an electron moves in a magnetic field, it experiences a magnetic force perpendicular to both its velocity and the magnetic field direction. This force can be calculated using the following equation:

\\[ F = q \\cdot v \\cdot B \\cdot \\sin(\\theta) \\]

Where:
- \\( F \\) is the magnetic force.
- \\( q \\) is the charge of the electron ({electron_charge:.2e} C).
- \\( v \\) is the velocity of the electron ({velocity:.2e} m/s).
- \\( B \\) is the magnetic field strength ({magnetic_field_strength:.2f} T).
- \\( \\theta \\) is the angle between the electron's velocity and the magnetic field.

To find \\( \\theta \\), we rearrange the equation:

\\[ \\theta = \\arcsin\\left(\\frac{{F}}{{q \\cdot v \\cdot B}}\\right) \\]

For the given values:
- Charge of an electron ({electron_charge:.2e} C)
- Velocity ({velocity:.2e} m/s)
- Magnetic Field Strength ({magnetic_field_strength:.2f} T)
- Magnetic Force ({magnetic_force:.2e} N)

The angle \\( \\theta \\) is approximately {angle_degrees:.2f} degrees.

This code calculates the trajectory of the electron and presents the results interactively.
"""

# Display the 3D plot
display(HTML("<h2>Electron Motion 3D Plot</h2>"))
fig_3d.show()

# Display the data table
display(HTML("<h2>Data Table</h2>"))
table.show()

# Display the explanation and theory
display(HTML(theory_text))
