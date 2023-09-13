import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
proton_velocity = 5.00e7  # m/s
force = 1.70e-16  # N
angle_deg = 45  # degrees

# Calculate the magnetic field strength (B)
angle_rad = np.deg2rad(angle_deg)
B = force / (proton_velocity * np.sin(angle_rad))

# Create a DataFrame for data analysis
data = {
    'Proton Velocity (m/s)': [proton_velocity],
    'Force (N)': [force],
    'Angle (degrees)': [angle_deg],
    'Magnetic Field (T)': [B]
}
df = pd.DataFrame(data)

# Data analysis
print("Data Analysis:")
print(df)

# Create a bar chart to visualize magnetic field strength vs. angle
fig1 = px.bar(df, x='Angle (degrees)', y='Magnetic Field (T)', title='Magnetic Field Strength vs. Angle')
fig1.show()

# Spherical coordinates for magnetic field direction
phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, np.pi, 100)
phi, theta = np.meshgrid(phi, theta)

# Magnetic field direction in spherical coordinates
x = B * np.sin(theta) * np.cos(phi)
y = B * np.sin(theta) * np.sin(phi)
z = B * np.cos(theta)

# Create a 3D surface plot to visualize magnetic field direction
fig2 = go.Figure(data=[go.Surface(x=x, y=y, z=z)])
fig2.update_layout(scene=dict(aspectratio=dict(x=1, y=1, z=1), aspectmode="cube"))
fig2.update_layout(title='Magnetic Field Direction')

# Create a 3D animation to show proton's motion
fig3 = plt.figure()
ax = fig3.add_subplot(111, projection='3d')

# Create an animation of proton's path through the magnetic field (you can use additional libraries like matplotlib.animation)
# Add labels, titles, and customize the plot as needed

# Show the 3D plot of magnetic field direction
fig2.show()

# Show the 3D animation of proton's motion
plt.show()
