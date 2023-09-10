import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the capacitor value (in Farads)
C = 0.500e-6  # 0.500 μF

# Define the range of resistor values
R_range = np.linspace(0.1, 10.0, 100)  # Change the range as needed

# Calculate time constants for the range of resistor values
time_constants = R_range * C

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the 3D surface
ax.plot(R_range, np.full_like(R_range, C), time_constants)

# Label the axes and provide a title
ax.set_xlabel('Resistor (Ohms)')
ax.set_ylabel('Capacitor (F)')
ax.set_zlabel('Time Constant (s)')
ax.set_title('Time Constant vs. Resistor and Capacitor')

# Show the plot
plt.show()
