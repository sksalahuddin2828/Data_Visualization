import matplotlib.pyplot as plt
import numpy as np

x_vals = np.linspace(-1, 1, 100)
n_vals = np.linspace(0.1, 5, 100)
X, N = np.meshgrid(x_vals, n_vals)
Z = (1 + X)**(-N)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, N, Z)
plt.xlabel('x')
plt.ylabel('n')
plt.title('3D Plot of (1+x)^(-n)')
plt.show()
