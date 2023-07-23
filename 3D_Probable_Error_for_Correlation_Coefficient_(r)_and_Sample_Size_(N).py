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
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(R, N, pe_values, cmap='plasma', rstride=1, cstride=1, linewidth=0, antialiased=True)

# Add artistic elements and annotations
ax.set_xlabel('Correlation Coefficient (r)')
ax.set_ylabel('Sample Size (N)')
ax.set_zlabel('Probable Error (P.E.)')
ax.set_title('Probable Error for Correlation Coefficient (r) and Sample Size (N)')
ax.text(-1.2, 200, 0.04, "P.E. = 0.674 * (1 - r^2) / sqrt(N)", color='white', fontsize=12)

# Customize the colorbar
cbar = plt.colorbar(surf, shrink=0.5, aspect=10)
cbar.set_label('Probable Error (P.E.)', rotation=270, labelpad=15)

# Add mathematical dance or equations if desired
ax.text(0, 100, 0.02, r"$P.E. = \frac{{0.674 \cdot (1 - r^2)}}{{\sqrt{N}}}$", color='white', fontsize=16)

# Show the plot
plt.show()
