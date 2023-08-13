import numpy as np

# Define the matrix
A = np.array([[1, 2], [3, 4]])

# Calculate the determinant
det_A = np.linalg.det(A)
print(det_A)

import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2], [3, 4]])

plt.imshow(A, cmap='viridis')
plt.colorbar()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

plt.show()
