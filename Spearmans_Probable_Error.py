import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Function to calculate the probable error for ρ (rho) using the Spearman method
def probable_error_spearman(rho, N):
    rho_squared = rho**2
    pe = 0.6745 * (1 - rho_squared) / (np.sqrt(N) * (1 + 1.086*rho_squared + 0.13*rho_squared**2 + 0.002*rho_squared**3))
    return pe

# Generate data points for correlation coefficient (ρ) and sample size (N)
rho_values = np.linspace(-1, 1, 100)  # ρ (rho) range from -1 to 1
N_values = np.arange(10, 201, 10)    # Sample sizes from 10 to 200 with step 10

# Create a meshgrid from the data points
Rho, N = np.meshgrid(rho_values, N_values)

# Calculate the probable error for each combination of ρ and N
pe_values = probable_error_spearman(Rho, N)

# 3D Visualization using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Rho, N, pe_values, cmap='plasma')

# Customize the plot
ax.set_xlabel('Correlation Coefficient (ρ)')
ax.set_ylabel('Sample Size (N)')
ax.set_zlabel('Probable Error (P.E.)')
ax.set_title('Spearman\'s Probable Error')

# Show the plot
plt.show()
