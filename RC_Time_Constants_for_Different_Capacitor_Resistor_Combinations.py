import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Capacitor and resistor values
capacitors = [2.00e-6, 7.50e-6]
resistors = [25.0e3, 100.0e3]

# Initialize an empty list to store time constants
time_constants = []

# Calculate RC time constants for all possible combinations
for C in capacitors:
    for R in resistors:
        time_constant = R * C
        time_constants.append(time_constant)

# Create a 3D visualization of the time constants
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Separate time constants into components for plotting
R_values = [R for _ in resistors for R in resistors]
C_values = [C for C in capacitors * len(resistors)]
time_constants = np.array(time_constants)

# Plot the time constants in 3D
ax.scatter(R_values, C_values, time_constants, c='b', marker='o')

# Set axis labels
ax.set_xlabel('Resistance (Ohms)')
ax.set_ylabel('Capacitance (Farads)')
ax.set_zlabel('RC Time Constant (s)')

plt.title('RC Time Constants for Different Capacitor-Resistor Combinations')
plt.show()
