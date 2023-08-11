import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_vals = np.linspace(-10, 10, 100)
y_vals = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z_eq1 = (19 - 4*X - 5*Y) / 5
Z_eq2 = 10*X - 2*Y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z_eq1, cmap='viridis', alpha=0.5)
ax.plot_surface(X, Y, Z_eq2, cmap='plasma', alpha=0.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.title('3D Visualization of Linear Equations')
plt.show()

