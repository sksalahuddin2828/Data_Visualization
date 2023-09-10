import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
emf_standard = 3.0  # Standard EMF in volts
rs_values = np.linspace(10.0, 20.0, 50)  # Range of Rs values from 10.0 Ω to 20.0 Ω
emfx_values = np.linspace(0.0, 5.0, 50)  # Range of unknown EMF values from 0.0 V to 5.0 V

# Create a grid of Rs and EMFx values
rs_grid, emfx_grid = np.meshgrid(rs_values, emfx_values)

# Calculate corresponding Rx values using the potentiometer formula
rx_grid = emfx_grid * (rs_grid / emf_standard - 1)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(rs_grid, emfx_grid, rx_grid, cmap='viridis')

# Add labels and title
ax.set_xlabel('Rs (Ω)')
ax.set_ylabel('EMFx (V)')
ax.set_zlabel('Rx (Ω)')
plt.title('3D Visualization of Potentiometer Balance')

# Show the plot
plt.show()

# Now, let's find the Rx value for emfx = 3.1 V and Rs = 15.0 Ω
target_emfx = 3.1
target_rs = 15.0

# Interpolate the Rx value
from scipy.interpolate import griddata
target_rx = griddata((rs_grid.ravel(), emfx_grid.ravel()), rx_grid.ravel(), (target_rs, target_emfx), method='linear')

print(f"For EMFx = {target_emfx} V and Rs = {target_rs} Ω, Rx = {target_rx:.2f} Ω")
