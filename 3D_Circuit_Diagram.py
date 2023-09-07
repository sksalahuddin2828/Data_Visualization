# R_s = (R_g / (I_full / I_g - 1))

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
R_g = 25.0  # Galvanometer resistance in ohms
I_g = 50e-6  # Galvanometer sensitivity in A
I_full = 10.0  # Full-scale current in A

# Calculate shunt resistance
R_s = R_g / (I_full / I_g - 1)

# Create a circuit diagram
fig, ax = plt.subplots()
ax.plot([0, 1], [0, 0], 'ro-', label='Galvanometer (G)')
ax.plot([0, 1], [0, 0], 'bo-', label='Shunt Resistor (R_s)')
ax.legend()
ax.set_xlim(-0.1, 1.1)
ax.set_ylim(-0.1, 0.1)
ax.set_aspect('equal', adjustable='box')
plt.title('Circuit Diagram')

# Create a 3D plot for R_s vs. I_full
R_s_values = np.linspace(0, 50, 100)  # Adjust the range as needed
I_full_values = np.linspace(1, 20, 100)  # Adjust the range as needed
R_s_mesh, I_full_mesh = np.meshgrid(R_s_values, I_full_values)
I_g_calculated = R_g / (R_s_mesh + R_g) * I_full_mesh

fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')
ax_3d.plot_surface(R_s_mesh, I_full_mesh, I_g_calculated, cmap='viridis')
ax_3d.set_xlabel('Shunt Resistance (R_s) [Ω]')
ax_3d.set_ylabel('Full-scale Current (I_full) [A]')
ax_3d.set_zlabel('Galvanometer Current (I_g) [A]')
plt.title('3D Plot')

# Show the plots
plt.show()
