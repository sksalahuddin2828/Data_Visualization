import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate probable error
def probable_error(r, N):
    return 0.674 * (1 - r**2) / np.sqrt(N)

# Sample data for correlation coefficient 'r' and sample size 'N'
r = 0.8
N = 100

# Calculate probable error
p_error = probable_error(r, N)

# Visualization - 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a meshgrid for 'r' and 'N' values
r_values = np.linspace(-1, 1, 100)
N_values = np.arange(2, 101)

R, N = np.meshgrid(r_values, N_values)
P_error = probable_error(R, N)

# Plot the 3D surface
ax.plot_surface(R, N, P_error, cmap='viridis')

# Add labels and title
ax.set_xlabel('Correlation Coefficient (r)')
ax.set_ylabel('Sample Size (N)')
ax.set_zlabel('Probable Error')
ax.set_title('Probable Error for Correlation Coefficient')

# Show the plot
plt.show()
