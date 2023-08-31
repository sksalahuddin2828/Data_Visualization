import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
import torch
from sklearn import datasets
from scipy.optimize import fsolve

# Define symbols
R1, R2, Rs, Rp = sp.symbols('R1 R2 Rs Rp')

# Equations
Rs_equation = sp.Eq(Rs, R1 + R2)
Rp_equation = sp.Eq(1/Rp, 1/R1 + 1/R2)

# Parameters
R1_val = 4.0
R2_val = 2.0

# Solve for Rs
Rs_solution = sp.solve(Rs_equation.subs({R1: R1_val, R2: R2_val}), Rs)
Rs_value = Rs_solution[0].evalf()

# Solve for Rp
Rp_solution = sp.solve(Rp_equation.subs({R1: R1_val, R2: R2_val}), Rp)
Rp_value = Rp_solution[0].evalf()

# Calculate approximate values
Rs_approx = R1_val * (R1_val / R2_val)
Rp_approx = R2_val * (R1_val / R2_val)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for R1 and R2
R1_vals = np.linspace(1, 10, 100)
R2_vals = np.linspace(1, 10, 100)
R1_mesh, R2_mesh = np.meshgrid(R1_vals, R2_vals)

# Calculate Rs and Rp using meshgrid values
Rs_mesh = R1_mesh + R2_mesh
Rp_mesh = R1_mesh * R2_mesh / (R1_mesh + R2_mesh)

# Plot Rs and Rp surfaces
ax.plot_surface(R1_mesh, R2_mesh, Rs_mesh, cmap='viridis', alpha=0.8)
ax.plot_surface(R1_mesh, R2_mesh, Rp_mesh, cmap='plasma', alpha=0.8)

# Set labels and title
ax.set_xlabel('R1')
ax.set_ylabel('R2')
ax.set_zlabel('Rs and Rp')
ax.set_title('Rs and Rp Surfaces')

# Show the plot
plt.show()

# Create a DataFrame for interactive visualization
df = pd.DataFrame({'R1': R1_mesh.flatten(), 'R2': R2_mesh.flatten(), 'Rs': Rs_mesh.flatten(), 'Rp': Rp_mesh.flatten()})

# Create an interactive scatter plot
scatter_fig = px.scatter_3d(df, x='R1', y='R2', z='Rs', color='Rs', title='Rs 3D Scatter Plot')
scatter_fig.update_layout(scene=dict(zaxis_title='Rs'))

# Create an interactive surface plot for Rp
surface_fig = px.scatter_3d(df, x='R1', y='R2', z='Rp', color='Rp', title='Rp Surface Plot')
surface_fig.update_layout(scene=dict(zaxis_title='Rp'))

# Show the interactive plots
scatter_fig.show()
surface_fig.show()
