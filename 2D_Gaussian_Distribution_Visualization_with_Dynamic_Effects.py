# 2D Gaussian Distribution Visualization with Dynamic Effects

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
exp_term = np.einsum('...k,kl,...l->...', pos - mean, inv_cov, pos - mean)
Z = np.exp(-0.5 * exp_term) / (2 * np.pi * np.sqrt(det))

# Create the main plot for the Gaussian distribution
fig, ax = plt.subplots()
im = ax.imshow(Z, cmap='viridis', extent=[-5, 5, -5, 5], origin='lower', aspect='auto')

# Add color bar
cbar = plt.colorbar(im)
cbar.set_label('Probability Density')

# Add title and labels
ax.set_title('2D Gaussian Distribution')
ax.set_xlabel('X')
ax.set_ylabel('Y')

# Create a subplot for probability contours
ax_prob_contour = fig.add_subplot(222)
contour = ax_prob_contour.contour(X, Y, Z, cmap='viridis')
ax_prob_contour.set_title('Probability Contour')
ax_prob_contour.set_xlabel('X')
ax_prob_contour.set_ylabel('Y')

# Calculate and display mean and standard deviation
mean_x, mean_y = mean
std_x = np.sqrt(covariance_matrix[0, 0])
std_y = np.sqrt(covariance_matrix[1, 1])

ax.text(0.05, 0.95, f'Mean (X, Y): ({mean_x:.2f}, {mean_y:.2f})', transform=ax.transAxes)
ax.text(0.05, 0.90, f'Standard Deviation (X): {std_x:.2f}', transform=ax.transAxes)
ax.text(0.05, 0.85, f'Standard Deviation (Y): {std_y:.2f}', transform=ax.transAxes)

# Update function for the animation
def update(num):
    # Update the Z values with a time-dependent parameter (for dynamic effect)
    time_param = np.sin(num * 0.1)  # Replace this with your dynamic factor
    updated_Z = Z * time_param

    # Update the main plot with the new Z values
    im.set_data(updated_Z)

    # Update the probability contour plot
    for coll in contour.collections:
        coll.remove()
    contour = ax_prob_contour.contour(X, Y, updated_Z, cmap='viridis')

    # Return the plot objects to be redrawn
    return im, contour.collections

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

# Show the animation
plt.show()
