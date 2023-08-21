import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

x_vals = np.linspace(-10, 10, 400)

x, a = sp.symbols('x a')
integral_expr = a**2 - x**2
integral_result_positive = sp.integrate(sp.sqrt(integral_expr), x)
integral_result_negative = -sp.integrate(sp.sqrt(integral_expr), x)

X, A = np.meshgrid(x_vals, x_vals)
Z_positive = np.array([[abs(integral_result_positive.subs({x: x_val, a: a_val}).evalf()) for x_val in x_vals] for a_val in x_vals])
Z_negative = np.array([[abs(integral_result_negative.subs({x: x_val, a: a_val}).evalf()) for x_val in x_vals] for a_val in x_vals])

fig_3d_positive = plt.figure()
ax_positive = fig_3d_positive.add_subplot(111, projection='3d')
ax_positive.plot_surface(X, A, Z_positive, cmap='viridis')
ax_positive.set_xlabel('x')
ax_positive.set_ylabel('a')
ax_positive.set_zlabel('Integral Value')
ax_positive.set_title('Positive Branch 3D Integral Visualization')
plt.show()

fig_3d_negative = plt.figure()
ax_negative = fig_3d_negative.add_subplot(111, projection='3d')
ax_negative.plot_surface(X, A, Z_negative, cmap='plasma')
ax_negative.set_xlabel('x')
ax_negative.set_ylabel('a')
ax_negative.set_zlabel('Integral Value')
ax_negative.set_title('Negative Branch 3D Integral Visualization')
plt.show()
