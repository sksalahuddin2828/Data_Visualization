import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

K = sp.symbols('K')
recurrence_relation = K**4 + 4*K**3 + 8*K**2 + 8*K + 4

roots = sp.solve(recurrence_relation, K)
print("Roots of the equation:", roots)

# Create meshgrid for 3D visualization
K_values = np.linspace(-5, 5, 100)
K, K_values = np.meshgrid(K_values, K_values)

# Evaluate the equation at each point
Z = K**4 + 4*K**3 + 8*K**2 + 8*K + 4

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(K, K_values, Z, cmap='viridis')
ax.set_xlabel('K')
ax.set_ylabel('K_values')
ax.set_zlabel('Value')
ax.set_title('3D Visualization of the Difference Equation')
plt.show()
