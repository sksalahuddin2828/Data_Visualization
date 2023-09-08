import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.cm import ScalarMappable

# Constants
emf = 3.200  # EMF of the lithium cell in volts
internal_resistance = 5.00  # Internal resistance in ohms
voltmeter_resistance = 1000.0  # Voltmeter resistance in ohms

# (a) Calculate the current flowing through the circuit
voltage_values = np.linspace(0, emf, 100)
current_values = (emf - voltage_values) / (internal_resistance + voltmeter_resistance)

# (b) Calculate the terminal voltage
terminal_voltage = emf - current_values * internal_resistance

# (c) Calculate the ratio of measured terminal voltage to EMF
ratio = terminal_voltage / emf

# Create a 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the current as a function of voltage with labels
scatter = ax.scatter(voltage_values, current_values, ratio, c=ratio, cmap='viridis', label='Data Points')

ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Current (A)')
ax.set_zlabel('Ratio')
plt.title('Current, Voltage, and Ratio Relationship')

# Add colorbar for the ratio
sm = ScalarMappable(cmap='viridis')
sm.set_array(ratio)
cbar = plt.colorbar(sm)
cbar.set_label('Ratio')

plt.legend()
plt.show()
