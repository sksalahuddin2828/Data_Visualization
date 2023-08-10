import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create data points
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
x, y = np.meshgrid(x, y)
z = x**2 + y**2

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface with color map
surface = ax.plot_surface(x, y, z, cmap='viridis')

# Add contour lines
contours = ax.contour(x, y, z, zdir='z', offset=0, cmap='viridis', linewidths=0.5)

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Creative 3D Plot: z = x^2 + y^2')

# Add color bar
fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

# Animate rotation
def rotate_plot(i):
    ax.view_init(elev=30, azim=i)

# Create animation
from matplotlib.animation import FuncAnimation
animation = FuncAnimation(fig, rotate_plot, frames=np.arange(0, 360, 5), interval=100)

# Show the animated plot
plt.show()
