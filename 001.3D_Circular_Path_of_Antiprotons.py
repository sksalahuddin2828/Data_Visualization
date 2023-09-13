import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Given parameters
velocity = 5.00e7  # m/s
radius = 2.00  # m

# Mass and charge of antiprotons
mass_antiproton = 1.6726219e-27  # kg (same as proton)
charge_antiproton = -1.60217662e-19  # C (opposite of proton)

# Calculate the magnetic field strength using the centripetal force equation
centripetal_force = mass_antiproton * velocity**2 / radius
magnetic_field_strength = centripetal_force / abs(charge_antiproton)

print(f"The required magnetic field strength is {magnetic_field_strength:.2e} Tesla")

# Calculate the circular path coordinates
theta = np.linspace(0, 2 * np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)
z = np.zeros_like(x)

# Create a Pandas DataFrame to store the coordinates
data = pd.DataFrame({'X': x, 'Y': y, 'Z': z})

# Create an interactive 3D visualization using Plotly
fig = px.line_3d(data, x='X', y='Y', z='Z', title='Circular Path of Antiprotons')
fig.update_traces(marker=dict(size=3), line=dict(color='blue'), selector=dict(mode='lines+markers'))

# Adding annotations for better visualization
fig.add_trace(go.Scatter3d(
    x=[0], y=[0], z=[0],
    mode='text+markers',
    text=['Starship Enterprise'],
    marker=dict(size=4, color='blue')
))

fig.add_trace(go.Scatter3d(
    x=[radius], y=[0], z=[0],
    mode='text+markers',
    text=['Antiproton Path'],
    marker=dict(size=4, color='red')
))

fig.update_layout(scene=dict(aspectmode='cube'))
fig.show()
