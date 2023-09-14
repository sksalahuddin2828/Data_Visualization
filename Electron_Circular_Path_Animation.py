import numpy as np
import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Constants
velocity = 7.50e6  # m/s
magnetic_field_strength = 1.00e-5  # T
electron_charge = -1.602e-19  # C (charge of an electron)
electron_mass = 9.109e-31  # kg (mass of an electron)

# Function to calculate the radius of the circular path
def calculate_radius(velocity, magnetic_field_strength, electron_charge, electron_mass):
    return (electron_mass * velocity) / (np.abs(electron_charge) * magnetic_field_strength)

# Create a range of altitudes (z-values) to simulate motion in 3D
altitude_range = np.linspace(0, 2 * np.pi, 1000)
radius = calculate_radius(velocity, magnetic_field_strength, electron_charge, electron_mass)

# Calculate the electron's position in 3D space
x = radius * np.cos(altitude_range)
y = radius * np.sin(altitude_range)
z = altitude_range

# Create a pandas DataFrame to store electron's position data
electron_path = pd.DataFrame({'X': x, 'Y': y, 'Z': z})

# Create an animation of the electron's circular path
fig = make_subplots(rows=1, cols=1, specs=[[{'type': 'scatter3d'}]])
scatter = go.Scatter3d(x=electron_path['X'], y=electron_path['Y'], z=electron_path['Z'], mode='lines',
                       marker=dict(size=4), line=dict(width=3))

fig.add_trace(scatter)
fig.update_layout(scene=dict(aspectmode="cube"))
fig.update_layout(scene=dict(xaxis_title='X position (m)', yaxis_title='Y position (m)', zaxis_title='Altitude (m)'))
fig.update_layout(title='Electron Circular Path Animation')

# Add mathematical expression for the radius
radius_expression = r'$\frac{m_e \cdot v}{|q| \cdot B}$'
radius_formula = f'Radius = {radius:.2f} meters'

# Add explanations and equations
explanation_text = """
The electron follows a circular path due to the Lorentz force in a magnetic field.
The radius of the circular path is given by the formula:
"""
explanation_text += f"{radius_expression}\n"
explanation_text += f"{radius_formula}"

# Show the animation and additional information
fig.show()

print(explanation_text)
