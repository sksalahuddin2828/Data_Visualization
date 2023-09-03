import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Input values
V = 12.0  # Voltage
R1, R2, R3 = 1.0, 6.0, 13.0  # Resistances

# Calculate currents
I1 = V / R1
I2 = V / R2
I3 = V / R3

# Calculate powers
P1 = (V**2) / R1
P2 = (V**2) / R2
P3 = (V**2) / R3

# Create a pandas DataFrame
data = {
    'Resistor': ['R1', 'R2', 'R3'],
    'Resistance (Ω)': [R1, R2, R3],
    'Current (A)': [I1, I2, I3],
    'Power (W)': [P1, P2, P3]
}
df = pd.DataFrame(data)

# Visualization
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122)

# 3D Visualization of the circuit
# Customize your 3D visualization here (e.g., plot resistors, voltage sources, etc.)
resistor_positions = [(0, 0, 0), (1, 0, 0), (7, 0, 0)]  # Coordinates of resistor positions
resistor_lengths = [1, 6, 13]  # Lengths of resistors
current_positions = [(0.5, 0, 0), (3.5, 0, 0), (15, 0, 0)]  # Coordinates of current arrows
current_lengths = [I1, I2, I3]  # Lengths of current arrows

for i in range(len(resistor_positions)):
    ax1.plot([resistor_positions[i][0], resistor_positions[i][0] + resistor_lengths[i]], [0, 0], [0, 0], linewidth=5, color='gray')

for i in range(len(current_positions)):
    ax1.quiver(current_positions[i][0], 0, 0, 0, 0, current_lengths[i], color='blue', arrow_length_ratio=0.2)

ax1.set_xlim(0, 25)
ax1.set_ylim(-1, 1)
ax1.set_zlim(-1, 1)
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
ax1.set_title('3D Visualization of the Circuit')

# Display equations, formulas, and explanations as text or labels
equations = [
    f'I1 = {I1:.2f} A',
    f'I2 = {I2:.2f} A',
    f'I3 = {I3:.2f} A',
    f'P1 = {P1:.2f} W',
    f'P2 = {P2:.2f} W',
    f'P3 = {P3:.2f} W'
]
ax2.axis('off')
ax2.text(0.1, 0.6, '\n'.join(equations), fontsize=12, bbox={'facecolor': 'lightgray', 'alpha': 0.7})

# Customize the appearance for a beautiful and creative design
plt.show()
