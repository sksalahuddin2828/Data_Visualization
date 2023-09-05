import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
total_emf = 12.0  # Total EMF of the automobile battery in volts
num_cells = 6    # Number of lead-acid cells in series

# Calculate the EMF of an individual cell
emf_individual_cell = total_emf / num_cells

# Create a 3D plot to visualize the EMF of an individual cell
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Generate data points for the 3D plot
x = np.linspace(0, 1, 10)  # Varying cell resistance
y = np.linspace(0, 1, 10)  # Varying internal voltage drop
X, Y = np.meshgrid(x, y)
Z = emf_individual_cell - X * emf_individual_cell - Y * emf_individual_cell

# Plot the 3D surface
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Add labels and title
ax.set_xlabel('Cell Resistance')
ax.set_ylabel('Internal Voltage Drop')
ax.set_zlabel('EMF of Individual Cell (V)')
ax.set_title('EMF of an Individual Lead-Acid Cell')

# Show the plot
plt.show()
