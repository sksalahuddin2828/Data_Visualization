import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(n):
    while n % 2 != 0:
        n = 3 * n + 2
    return n // 2

# Generate data points for visualization
num_points = 1000
n_values = np.arange(num_points)
x_values, y_values, z_values = [], [], []

for n in n_values:
    x = n
    y = f(n)
    z = n % 2  # Color points differently based on parity (even or odd)
    x_values.append(x)
    y_values.append(y)
    z_values.append(z)

# Create a 3D scatter plot for visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Adjust marker size and color map
marker_size = 10
cmap = plt.cm.get_cmap('viridis', 2)  # Use 2 colors based on parity (even or odd)

# Scatter plot
ax.scatter(x_values, y_values, z_values, c=z_values, cmap=cmap, s=marker_size)

# Labels and title
ax.set_xlabel('n')
ax.set_ylabel('f(n)')
ax.set_zlabel('Parity (0: even, 1: odd)')
ax.set_title('Iteration of Number Theoretic Function f(2n)=n, f(2n+1)=f(3n+2)')

# Show the plot
plt.show()
