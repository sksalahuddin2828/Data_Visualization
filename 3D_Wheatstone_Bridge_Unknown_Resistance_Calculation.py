import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Simulated data for R1, R2, R3, and Rx
R1 = np.random.uniform(1, 10, 100)
R2 = np.random.uniform(1, 10, 100)
R3 = np.random.uniform(1, 10, 100)
Rx = (R3 * R2) / R1  # Calculate Rx using the Wheatstone bridge equation

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(R1, R2, Rx, c=Rx, cmap='viridis', label='Unknown Resistance (Rx)')

# Add labels and a color bar
ax.set_xlabel('R1')
ax.set_ylabel('R2')
ax.set_zlabel('Rx')
ax.set_title('Wheatstone Bridge - Unknown Resistance Calculation')
cbar = fig.colorbar(ax.scatter(R1, R2, Rx, c=Rx, cmap='viridis'), ax=ax)
cbar.set_label('Rx Value')

# Show the plot
plt.legend()
plt.show()
