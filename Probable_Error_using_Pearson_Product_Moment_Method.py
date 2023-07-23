import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate the probable error using the Pearson product-moment method
def probable_error(r, N):
    return 0.6745 * (1 - r**2) / np.sqrt(N)

# Create data points for correlation coefficient (r) and sample size (N)
r_values = np.linspace(-1, 1, 100)  # Correlation coefficient range from -1 to 1
N_values = np.arange(10, 201, 10)   # Sample sizes from 10 to 200 with step 10

# Create a meshgrid from the data points
R, N = np.meshgrid(r_values, N_values)

# Calculate the probable error for each combination of r and N
pe_values = probable_error(R, N)

# 3D Visualization using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(R, N, pe_values, cmap='viridis')

# Customize the plot
ax.set_xlabel('Correlation Coefficient (r)')
ax.set_ylabel('Sample Size (N)')
ax.set_zlabel('Probable Error (P.E.)')
ax.set_title('Probable Error using Pearson Product-Moment Method')

# Show the plot
plt.show()
