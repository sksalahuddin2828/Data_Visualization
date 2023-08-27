import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Calculate peak current
rms_current = 15.0
peak_current = rms_current * np.sqrt(2)

# Visualization
rms_values = np.linspace(0, 20, 100)
peak_values = rms_values * np.sqrt(2)

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

RMS, PEAK = np.meshgrid(rms_values, peak_values)
ax.plot_surface(RMS, PEAK, PEAK, cmap='viridis')

ax.set_xlabel('RMS Current (A)')
ax.set_ylabel('Peak Current (A)')
ax.set_zlabel('Peak Current (A)')
ax.set_title('RMS vs. Peak Current')

plt.show()
