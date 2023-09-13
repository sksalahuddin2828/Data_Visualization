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
