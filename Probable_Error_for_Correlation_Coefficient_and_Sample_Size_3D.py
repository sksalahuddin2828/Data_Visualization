import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate the probable error for 'r'
def probable_error(r, N):
    return 0.674 * (1 - r**2) / np.sqrt(N)

# Generate data points for correlation coefficient (r) and sample size (N)
r_values = np.linspace(-1, 1, 100)  # 'r' range from -1 to 1
N_values = np.arange(10, 201, 10)   # Sample sizes from 10 to 200 with step 10

# Create a meshgrid from the data points
R, N = np.meshgrid(r_values, N_values)

# Calculate the probable error for each combination of 'r' and 'N'
pe_values = probable_error(R, N)

# 3D Visualization using matplotlib
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create a colormap with vibrant colors
cmap = plt.get_cmap('viridis')

# Plot the 3D surface with the probable error values
surf = ax.plot_surface(R, N, pe_values, cmap=cmap, edgecolor='k')

# Add artistic elements and annotations
ax.set_xlabel('Correlation Coefficient (r)')
ax.set_ylabel('Sample Size (N)')
ax.set_zlabel('Probable Error (P.E.)')
ax.set_title('Probable Error for Correlation Coefficient and Sample Size')

# Add a colorbar with a beautiful color map
cbar = plt.colorbar(surf, shrink=0.5, aspect=10)
cbar.set_label('Probable Error (P.E.)', rotation=270, labelpad=15)

# Add a mathematical dance or equations with an artistic touch
ax.text(0, 100, 0.04, r"$P.E. = 0.674 \times \frac{{(1 - r^2)}}{{\sqrt{N}}}$", color='white', fontsize=16)

# Customize the plot aesthetics
ax.set_facecolor('#f0f0f0')
ax.grid(False)

# Add a light source to create shadows and depth in the plot
ax.view_init(elev=20, azim=30)

# Show the plot
plt.show()
