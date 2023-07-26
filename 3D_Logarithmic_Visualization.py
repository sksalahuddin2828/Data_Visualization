import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data for visualization
x = np.linspace(1, 10, 100)
y = np.log(x)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, np.zeros_like(x), c=y, cmap='viridis', marker='o')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Add a title and show the plot
plt.title('3D Logarithmic Visualization using Matplotlib')
plt.show()
