import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Define the parameters for the Gaussian distribution
mean = np.array([0, 0])  # Mean of the distribution (2D for now)
covariance_matrix = np.array([[1, 0.5], [0.5, 1]])  # Covariance matrix (2D for now)

# Create a meshgrid for the 2D plot
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))

# Calculate the Gaussian probability at each point in the meshgrid
det = np.linalg.det(covariance_matrix)
inv_cov = np.linalg.inv(covariance_matrix)
Z = np.exp(-0.5 * np.einsum('...k,kl,...l->...', pos - mean, inv_cov, pos - mean)) / (2 * np.pi * np.sqrt(det))

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create the surface plot
surface = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Set axis labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.set_title('2D Gaussian Distribution')

# Add a color bar
fig.colorbar(surface)

# Update function for the animation
def update(num):
    # Update the Z values with a time-dependent parameter
    time_param = np.sin(num * 0.1)  # Replace this with your 4D data source
    updated_Z = Z * time_param

    # Update the surface plot with the new Z values
    surface.set_array(updated_Z.ravel())

    # Return the plot objects to be redrawn
    return surface,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50, blit=True)

# Show the animation
plt.show()
