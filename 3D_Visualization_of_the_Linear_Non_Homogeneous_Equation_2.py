import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

r = sp.symbols('r')
recurrence_relation = r**2 + 2 - 4*r + 4 - (3*r + 2*r)

roots = sp.solve(recurrence_relation, r)
print("Roots of the equation:", roots)

# Create meshgrid for 3D visualization
r_values = np.linspace(-5, 5, 100)
r, R = np.meshgrid(r_values, r_values)

# Evaluate the equation at each point
Z = R**2 + 2 - 4*R + 4 - (3*R + 2*R)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(r, R, Z, cmap='viridis')
ax.set_xlabel('r')
ax.set_ylabel('R')
ax.set_zlabel('Value')
ax.set_title('3D Visualization of the Linear Non-Homogeneous Equation')
plt.show()
