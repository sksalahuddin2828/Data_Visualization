import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create a figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create data for the grid
alpha = np.linspace(0, 2 * np.pi, 100)
beta = np.linspace(0, 2 * np.pi, 100)
Alpha, Beta = np.meshgrid(alpha, beta)

# Calculate the values for the LHS and RHS of the identity
lhs = np.cos(Alpha + Beta)
rhs = np.cos(Alpha) * np.cos(Beta) - np.sin(Alpha) * np.sin(Beta)

# Create a 3D surface plot for the LHS
lhs_surface = ax.plot_surface(Alpha, Beta, lhs, cmap='coolwarm', alpha=0.7, label='lhs')

# Create a 3D surface plot for the RHS
rhs_surface = ax.plot_surface(Alpha, Beta, rhs, cmap='viridis', alpha=0.7, label='rhs')

# Set labels and title
ax.set_xlabel('Alpha')
ax.set_ylabel('Beta')
ax.set_zlabel('Value')
ax.set_title('Trigonometric Identity: cos(α±β) = cosαcosβ ∓ sinαsinβ')

# Add a color bar for the LHS
cbar_lhs = fig.colorbar(lhs_surface, ax=ax, pad=0.1, shrink=0.7)
cbar_lhs.set_label('Value')

# Show the plot
plt.show()
