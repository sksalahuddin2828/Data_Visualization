from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

# Matplotlib Visualization
x_vals = np.linspace(-2*np.pi, 2*np.pi, 400)
y_vals = np.log(np.abs(1/np.cos(x_vals)))

X, Y = np.meshgrid(x_vals, y_vals)
Z = np.log(np.abs(1/np.cos(X)))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('ln|sec(x)|')
ax.set_zlabel('Z')
ax.set_title('3D Visualization of ln|sec(x)|')
plt.show()
