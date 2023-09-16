import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 1: Generate a range of angles
angles = np.linspace(0.01, np.pi / 2, 100)  # 100 angles from 0.01 to π/2

# Step 2: Calculate Secant Values using SymPy
sec_values = [1 / sp.cos(angle) for angle in angles]

# Step 3: Data Visualization
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Plot the secant values
ax.plot(angles, [0] * len(sec_values), sec_values, label='sec(θ)', linewidth=2)

# Customize the plot
ax.set_xlabel('θ')
ax.set_ylabel('sec(θ)')
ax.set_zlabel('Value')
ax.set_title('Secant Function')
ax.legend()

# Add creative elements (e.g., annotation)
ax.text(np.pi / 4, 0, 3, "Secant Function", color='red', fontsize=12)

# Show the plot
plt.show()
