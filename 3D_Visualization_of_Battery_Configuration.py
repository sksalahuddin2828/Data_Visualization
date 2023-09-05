import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

emf_single_cell = 1.54  # EMF of a single cell in volts
desired_voltage = 9  # Desired battery voltage in volts

# Calculate the number of cells needed
num_cells = np.ceil(desired_voltage / emf_single_cell).astype(int)
print(f"(a) Number of cells needed: {num_cells}")

actual_emf = num_cells * emf_single_cell
print(f"(b) Actual EMF of the 9-V battery: {actual_emf} V")

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create data points
num_cells_range = np.arange(1, 20, 1)
emf_values = num_cells_range * emf_single_cell
num_cells_mesh, emf_mesh = np.meshgrid(num_cells_range, emf_values)
actual_emf_mesh = num_cells_mesh * emf_mesh

# Plot the 3D surface
ax.plot_surface(num_cells_mesh, emf_mesh, actual_emf_mesh, cmap='viridis')

# Add labels and title
ax.set_xlabel('Number of Cells')
ax.set_ylabel('EMF per Cell (V)')
ax.set_zlabel('Actual EMF (V)')
plt.title('3D Visualization of Battery Configuration')

# Show the plot
plt.show()

