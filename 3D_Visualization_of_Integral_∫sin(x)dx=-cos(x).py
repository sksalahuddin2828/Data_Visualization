import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

x_vals = np.linspace(0, 2*np.pi, 100)
y_vals = np.sin(x_vals)
z_vals = -np.cos(x_vals)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_vals, y_vals, z_vals, label='Integral: -cos(x)')
ax.set_xlabel('x')
ax.set_ylabel('sin(x)')
ax.set_zlabel('-cos(x)')
ax.set_title('3D Visualization of Integral ∫sin(x) dx = -cos(x)')
ax.legend()
plt.show()
