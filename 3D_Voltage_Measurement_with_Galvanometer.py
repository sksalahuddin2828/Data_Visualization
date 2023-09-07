import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
V_full_scale = 0.100  # Full-scale reading in volts
I_g_sensitivity = 50e-6  # Galvanometer sensitivity in amperes
G_internal_resistance = 25.0  # Internal resistance of the galvanometer in ohms

# Create a range of resistance values
R = np.linspace(0, 200, 100)  # You can adjust the range as needed

# Calculate the voltmeter reading for each resistance value
V_meter = V_full_scale / (1 + R / G_internal_resistance)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
X, Y = np.meshgrid(R, V_meter)
Z = I_g_sensitivity * (Y - V_full_scale) + G_internal_resistance * (Y / V_full_scale - 1)
ax.plot_surface(X, Y, Z, cmap='viridis')

# Label the axes
ax.set_xlabel('Series Resistance (Ω)')
ax.set_ylabel('Voltmeter Reading (V)')
ax.set_zlabel('Galvanometer Deflection (A)')

# Show the plot
plt.title('Voltage Measurement with Galvanometer')
plt.show()

# Find the minimum resistance needed for accurate measurement
min_R = R[np.argmin(np.abs(Z))]
print(f"The minimum series resistance needed for accurate measurement is {min_R:.2f} Ω")
