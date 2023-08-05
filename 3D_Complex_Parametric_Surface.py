import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, cos, sin, exp, lambdify

u, v = symbols('u v')
x = cos(u) * (2 + cos(3*v))
y = sin(u) * (2 + cos(3*v))
z = sin(3*v)

u_values = np.linspace(0, 2 * np.pi, 100)
v_values = np.linspace(0, 2 * np.pi, 100)
u_mesh, v_mesh = np.meshgrid(u_values, v_values)

x_eval = lambdify((u, v), x, 'numpy')
y_eval = lambdify((u, v), y, 'numpy')
z_eval = lambdify((u, v), z, 'numpy')

x_values = x_eval(u_mesh, v_mesh)
y_values = y_eval(u_mesh, v_mesh)
z_values = z_eval(u_mesh, v_mesh)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(x_values, y_values, z_values, cmap='viridis')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.title('Complex 3D Parametric Surface')
plt.show()
