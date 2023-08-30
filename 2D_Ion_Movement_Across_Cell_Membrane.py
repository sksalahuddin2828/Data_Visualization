import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
cell_thickness = 8e-9  # meters
voltage_difference = -90e-3  # Volts (interior - exterior)
electric_field = voltage_difference / cell_thickness  # V/m

# Simulating ion movements
time = np.linspace(0, 10, 100)  # Time steps
ion_concentration = np.linspace(0, 1, 100)  # Ion concentration gradient

# Create a meshgrid for time and ion_concentration
T, C = np.meshgrid(time, ion_concentration)

# Calculate ion movement based on diffusion and electric field
ion_movement = C * (electric_field + np.gradient(C, axis=0)[0])

# Create 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(T, C, ion_movement, cmap='viridis')
ax.set_xlabel('Time')
ax.set_ylabel('Ion Concentration')
ax.set_zlabel('Ion Movement')
ax.set_title('Ion Movement Across Cell Membrane')
plt.show()
