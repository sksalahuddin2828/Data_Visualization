import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import plotly.express as px

# Given values
Vrms = 220  # RMS voltage (V)
Irms = 2    # RMS current (A)
R = 50      # Resistance (ohms)

# Calculate average power using the provided expressions
Pave_1 = Irms * Vrms
Pave_2 = (Vrms ** 2) / R
Pave_3 = (Irms ** 2) * R

# Creating a sympy expression for Pave_1
I, V = sp.symbols('I V')
Pave_expr = I * V

# Create a beautiful sympy equation representation
equation_str = f'Pave = {sp.latex(Pave_expr.subs({I: Irms, V: Vrms}))}'

# Create a 3D visualization using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for the variables
I_vals = np.linspace(0, 4, 50)
V_vals = np.linspace(0, 250, 50)
I_mesh, V_mesh = np.meshgrid(I_vals, V_vals)
Pave_mesh = I_mesh * V_mesh

# Plot the 3D surface
ax.plot_surface(I_mesh, V_mesh, Pave_mesh, cmap='viridis')
ax.set_xlabel('Current (A)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Average Power (W)')
ax.set_title('Average Power in an AC Circuit')
plt.show()

# Create an interactive 3D visualization using Plotly
fig = px.scatter_3d(x=I_mesh.flatten(), y=V_mesh.flatten(), z=Pave_mesh.flatten(), color=Pave_mesh.flatten(), labels={'x': 'Current (A)', 'y': 'Voltage (V)', 'z': 'Average Power (W)'})
fig.update_layout(scene=dict(zaxis_title='Average Power (W)'))
fig.update_layout(coloraxis_colorbar_title='Average Power (W)')
fig.update_layout(title='Interactive Average Power Visualization')
fig.show()

# Print the equations
print(equation_str)
print(f'Pave_2 = {Pave_2} W')
print(f'Pave_3 = {Pave_3} W')
