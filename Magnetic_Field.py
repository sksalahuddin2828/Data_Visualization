import sympy as sp

# Define symbolic variables
q, v, B, F = sp.symbols('q v B F')

# Define the magnetic force equation
force_eq = sp.Eq(F, q * v * B)

# Substitute values and solve for F
q_value = 0.100e-6  # Charge in Coulombs
v_value = 5.00  # Speed in m/s
B_value = 1.50  # Magnetic field in Tesla

force_eq = force_eq.subs({q: q_value, v: v_value, B: B_value})
force = sp.solve(force_eq, F)

print("Maximum force on the rod:", force)

import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from sympy import symbols, Eq, solve

# Define symbolic variables
q, v, B, F = symbols('q v B F')

# Define the magnetic force equation
force_eq = Eq(F, q * v * B)

# Define problem-specific values
q_value = 0.100e-6  # Charge in Coulombs
v_value = 5.00  # Speed in m/s
B_value = 1.50  # Magnetic field in Tesla

# Substitute values and solve for F
force_eq = force_eq.subs({q: q_value, v: v_value, B: B_value})
force = solve(force_eq, F)[0]

# Display the force
print("Maximum force on the rod:", force)

# Create a 3D visualization of magnetic field vectors
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the magnetic field vector
B_vector = np.array([0, 0, B_value])

# Plot the magnetic field vector
ax.quiver(0, 0, 0, *B_vector, color='b', label='Magnetic Field (B)')

# Set plot limits and labels
ax.set_xlim([0, 2])
ax.set_ylim([0, 2])
ax.set_zlim([0, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()

# Create an interactive 3D visualization of magnetic field vectors using Plotly
fig = go.Figure()

# Define the magnetic field vector
B_vector = np.array([0, 0, B_value])

# Add magnetic field vector to the plotly figure
fig.add_trace(go.Scatter3d(x=[0, B_vector[0]], y=[0, B_vector[1]], z=[0, B_vector[2]],
                           mode='lines+text', line=dict(color='blue', width=5), text=['Origin', 'B']))

# Customize the layout
fig.update_layout(scene=dict(aspectmode='data'))
fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

# Show the interactive plotly figure
fig.show()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
mass_U235 = 3.90e-25  # Mass of uranium-235 ion (kg)
mass_U238 = 3.95e-25  # Mass of uranium-238 ion (kg)
velocity = 3.00e5      # Velocity of ions (m/s)
magnetic_field = 0.250  # Magnetic field strength (T)
charge_U235 = 3        # Charge of uranium-235 ion
charge_U238 = 3        # Charge of uranium-238 ion

# Calculate radius of semicircle path for each ion
radius_U235 = (mass_U235 * velocity) / (charge_U235 * magnetic_field)
radius_U238 = (mass_U238 * velocity) / (charge_U238 * magnetic_field)

# Calculate the separation between their paths when they hit a target
separation = radius_U238 - radius_U235

# Create a function to calculate positions of ions over time
def calculate_positions(time):
    angle_U235 = (velocity * time) / radius_U235
    angle_U238 = (velocity * time) / radius_U238
    x_U235 = radius_U235 * np.cos(angle_U235)
    y_U235 = radius_U235 * np.sin(angle_U235)
    x_U238 = radius_U238 * np.cos(angle_U238)
    y_U238 = radius_U238 * np.sin(angle_U238)
    return x_U235, y_U235, x_U238, y_U238

# Create an animation of ion paths
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(-1.2 * radius_U238, 1.2 * radius_U238)
ax.set_ylim(-1.2 * radius_U238, 1.2 * radius_U238)
line_U235, = ax.plot([], [], label='U-235 Path', linestyle='-', marker='o')
line_U238, = ax.plot([], [], label='U-238 Path', linestyle='-', marker='o')
plt.legend(loc='upper right')

def update(frame):
    x_U235, y_U235, x_U238, y_U238 = calculate_positions(frame)
    line_U235.set_data(x_U235, y_U235)
    line_U238.set_data(x_U238, y_U238)
    return line_U235, line_U238

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2 * np.pi, 100), interval=100)
plt.xlabel('X Position (m)')
plt.ylabel('Y Position (m)')
plt.title('Path of U-235 and U-238 Ions in a Magnetic Field')
plt.grid()
plt.show()

# Print the separation distance
print(f"Separation between paths: {separation:.4f} meters")
