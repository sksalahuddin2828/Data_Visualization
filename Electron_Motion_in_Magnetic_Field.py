# Import necessary libraries
import numpy as np
import sympy as sp
import pandas as pd
import plotly.graph_objs as go
from IPython.display import HTML, display

# Define constants
velocity = 4.00e3  # m/s
magnetic_field_strength = 1.25  # T
magnetic_force = 1.40e-16  # N
electron_charge = -1.602e-19  # C (charge of an electron)

# Calculate the angle using sympy
angle_symbolic = sp.asin(magnetic_force / (electron_charge * velocity * magnetic_field_strength))

# Convert the angle to degrees
angle_degrees = sp.deg(angle_symbolic)

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

# Create an interactive presentation using Plotly
presentation_text = f"The angle between velocity and magnetic field: {angle_degrees:.2f} degrees"
presentation_text += "<br>Equation: $\\theta = \\arcsin\\left(\\frac{F}{q \\cdot v \\cdot B}\\right)$"
presentation_text += f"<br>Angle (radians): {angle_symbolic.evalf()}"
presentation_text += f"<br>Magnetic Force (N): {magnetic_force}"
presentation_text += f"<br>Electron Charge (C): {electron_charge}"
presentation_text += f"<br>Velocity (m/s): {velocity}"
presentation_text += f"<br>Magnetic Field Strength (T): {magnetic_field_strength}"

# Create an interactive table with pandas DataFrame
table = go.Figure(data=[go.Table(header=dict(values=list(data.columns)),
                 cells=dict(values=[data['Time (s)'], data['X Position (m)']]))
                     ])
table.update_layout(title='Electron Motion Data Table')

# Display the 3D plot
display(HTML("<h2>Electron Motion 3D Plot</h2>"))
fig_3d.show()

# Display the data table
display(HTML("<h2>Data Table</h2>"))
table.show()

# Display the interactive presentation
display(HTML("<h2>Electron Motion Presentation</h2>"))
display(HTML(presentation_text))
