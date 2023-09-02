import sympy as sp

# Define variables
V = 12.0  # Total voltage
V1 = 2.35  # Voltage reduction
R2 = 6.00  # Resistance of R2

# Calculate Vp
Vp = V - V1

# Calculate current through R2
I2 = Vp / R2

print(f"Voltage applied to R2 (Vp): {Vp} V")
print(f"Current through R2 (I2): {I2} A")

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Create a grid of V1 and R2 values
V1_values = np.linspace(0, 5, 100)
R2_values = np.linspace(1, 10, 100)
V1_values, R2_values = np.meshgrid(V1_values, R2_values)

# Calculate corresponding I2 values using the formula
I2_values = (V - V1_values) / R2_values

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')  # Specify 3D projection
ax.plot_surface(V1_values, R2_values, I2_values, cmap='viridis')
ax.set_xlabel('V1 (V)')
ax.set_ylabel('R2 (Ω)')
ax.set_zlabel('I2 (A)')
ax.set_title('Current through R2 vs. V1 and R2')

plt.show()
