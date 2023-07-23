import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate the probable error for 'r' derived from 'ρ'
def probable_error_pearson(r, N):
    r_squared = r**2
    pe = 0.7063 * (1 - r_squared) * np.sqrt(N) * (1 + 1.042*r_squared + 0.008*r_squared**2 + 0.002*r_squared**3)
    return pe

# Generate data points for 'ρ' and sample size 'N'
rho_values = np.linspace(-1, 1, 100)  # 'ρ' (rho) range from -1 to 1
N_values = np.arange(10, 201, 10)    # Sample sizes from 10 to 200 with step 10

# Create a meshgrid from the data points
Rho, N = np.meshgrid(rho_values, N_values)

# Calculate the Pearson coefficient 'r' using the transmutation formula
r_values = 2 * np.sin(np.pi * Rho / 6)

# Calculate the probable error for each combination of 'r' and 'N'
pe_values = probable_error_pearson(r_values, N)

# 3D Visualization using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Rho, N, pe_values, cmap='inferno')

# Customize the plot
ax.set_xlabel('Correlation Coefficient (ρ)')
ax.set_ylabel('Sample Size (N)')
ax.set_zlabel('Probable Error (P.E.)')
ax.set_title('Probable Error for Pearson coefficient (r) from ρ using Transmutation Formula')

# Show the plot
plt.show()
