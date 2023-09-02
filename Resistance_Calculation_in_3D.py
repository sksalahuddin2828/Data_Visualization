import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the resistor values
R1 = 1.00
R2 = 6.00
R3 = 13.0

# Calculate Rp (parallel combination of R2 and R3)
Rp = 1 / (1/R2 + 1/R3)

# Calculate the total resistance
Rtot = R1 + Rp

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the coordinates for R2 and R3 values
R2_values = np.linspace(1, 10, 100)
R3_values = np.linspace(1, 20, 100)
R2_values, R3_values = np.meshgrid(R2_values, R3_values)
Rp_values = 1 / (1/R2_values + 1/R3_values)

# Plot the 3D surface
ax.plot_surface(R2_values, R3_values, Rp_values, cmap='viridis')
ax.set_xlabel('R2 (Ω)')
ax.set_ylabel('R3 (Ω)')
ax.set_zlabel('Rp (Ω)')
plt.title('Resistance Calculation in 3D')
plt.show()
