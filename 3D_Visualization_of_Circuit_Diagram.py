import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
R1 = 0.0200  # Resistance of ammeter in ohms
R2 = 10.00   # Resistance of the resistor in ohms
V = 12.0     # Voltage in volts (you can change this as needed)

# Part (a): Draw a Circuit Diagram (Basic Visualization)
fig, ax = plt.subplots()
ax.plot([0, R1 + R2], [0, 0], 'ro-', markersize=10, label='Ammeter')
ax.plot([R1 + R2, R1 + R2 + R2], [0, 0], 'bo-', markersize=10, label='Resistor')
ax.annotate('V', (R1 / 2, 0.1), fontsize=12)
ax.annotate('R1', (R1 / 2, -0.2), fontsize=12)
ax.annotate('R2', (R1 + R2 + R2 / 2, -0.2), fontsize=12)
ax.set_xlim(0, R1 + R2 + R2)
ax.set_ylim(-0.5, 0.5)
ax.set_xlabel('Circuit', fontsize=14)
ax.legend(loc='upper right')
plt.title('Circuit Diagram', fontsize=16)
plt.grid()
plt.show()

# Part (b): Calculate Resistance of the Combination
R_total = R1 + R2

# Part (c): Calculate Percent Decrease in Current
I1 = V / R2
I2 = V / R_total
percent_decrease_current = ((I1 - I2) / I1) * 100

# Part (d): Calculate Percent Increase in Voltage
V1 = I1 * R2
V2 = I2 * R_total
percent_increase_voltage = ((V2 - V1) / V1) * 100

# Part (f): Create a 3D Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(R1, R2, R_total, c='r', marker='o', label='R_total', s=100)
ax.set_xlabel('R1 (Ammeter Resistance)')
ax.set_ylabel('R2 (Resistor Resistance)')
ax.set_zlabel('R_total (Total Resistance)')
plt.title('3D Visualization of Resistance')
ax.legend(loc='upper right')
plt.show()

# Display results and visualizations
print("Total Resistance (R_total): {:.4f} ohms".format(R_total))
print("Percent Decrease in Current: {:.2f}%".format(percent_decrease_current))
print("Percent Increase in Voltage: {:.2f}%".format(percent_increase_voltage))
