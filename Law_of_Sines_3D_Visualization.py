import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define angle values
alpha_vals = np.linspace(0, np.pi/2, 100)
beta_vals = np.linspace(0, np.pi/2, 100)
alpha_mesh, beta_mesh = np.meshgrid(alpha_vals, beta_vals)

# Calculate corresponding gamma values using the Law of Sines
gamma_mesh = np.arcsin((np.sin(alpha_mesh) * np.sin(beta_mesh)) / np.sin(np.pi - alpha_mesh - beta_mesh))

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(alpha_mesh, beta_mesh, gamma_mesh, cmap='viridis')

# Set labels and title
ax.set_xlabel('Angle α')
ax.set_ylabel('Angle β')
ax.set_zlabel('Angle γ')
ax.set_title('Law of Sines 3D Visualization')

plt.show()
