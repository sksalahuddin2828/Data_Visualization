import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

a = sp.symbols('a')
recurrence_relation = a**3 + 6*a**2 + 12*a + 8

roots = sp.solve(recurrence_relation, a)
print("Roots of the equation:", roots)

# Create meshgrid for 3D visualization
a_values = np.linspace(-5, 5, 100)
a, A = np.meshgrid(a_values, a_values)

# Evaluate the equation at each point
Z = A**3 + 6*A**2 + 12*A + 8

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(a, A, Z, cmap='viridis')
ax.set_xlabel('a')
ax.set_ylabel('A')
ax.set_zlabel('Value')
ax.set_title('3D Visualization of the Linear Non-Homogeneous Equation')
plt.show()
