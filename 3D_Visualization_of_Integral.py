import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a meshgrid for x and m values
x_vals = np.linspace(0.1, 5, 100)
m_vals = np.linspace(-2, 2, 100)
X, M = np.meshgrid(x_vals, m_vals)

# Calculate the z values (integral results)
Z = X**M

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, M, Z, cmap='viridis')

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('m')
ax.set_zlabel('Integral Result')
ax.set_title('3D Visualization of Integral')

# Show the plot
plt.show()
