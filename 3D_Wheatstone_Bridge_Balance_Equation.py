import numpy as np
import sympy as sp

# Define the symbols
Rx, R1, R2, R3 = sp.symbols('Rx R1 R2 R3')

# Given ratio R2/R1
ratio = 0.625

# Balance equation for the Wheatstone bridge
balance_equation = sp.Eq(R2 / R1, (R3 / Rx))

# Solve for Rx
solution = sp.solve(balance_equation.subs(R2 / R1, ratio), Rx)

# Print the solution
print("Rx =", solution[0])

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid of values for R1, R2, and Rx
R1_values = np.linspace(1, 1000, 100)
R2_values = R1_values * ratio
Rx_values = np.linspace(1, 1000, 100)

# Calculate R3 values based on the balance equation
R3_values = (R2_values / ratio) * Rx_values

# Plot the 3D surface
ax.plot_surface(R1_values, R2_values, Rx_values.reshape(-1, 1), cmap='viridis')

# Set axis labels
ax.set_xlabel('R1')
ax.set_ylabel('R2')
ax.set_zlabel('Rx')

# Show the plot
plt.show()
