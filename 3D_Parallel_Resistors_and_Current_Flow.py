import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches

# Define the values
V = 12.0  # Voltage
R1 = 4.0  # Resistance 1
R2 = 6.0  # Resistance 2
R3 = 8.0  # Resistance 3

# Calculate the total current
I = V / (R1 + R2 + R3)

# Calculate the equivalent parallel resistance
Rp = 1 / (1 / R1 + 1 / R2 + 1 / R3)

# Create a 3D plot to visualize the circuit
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Coordinates for the resistors
resistor_coordinates = [(1, 0, 0), (2, 0, 0), (3, 0, 0)]

# Plot the resistors as cylinders
for i, (x, y, z) in enumerate(resistor_coordinates):
    ax.bar3d(x, y, z, 0.1, 0.1, I, shade=True, color='b', alpha=0.5, label=f'Resistor {i+1}')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Current (I)')
ax.set_title('Parallel Resistors and Current Flow')

# Display the equivalent parallel resistance
ax.text(1.5, 0, I / 2, f'Rp = {Rp:.2f} ohms', color='r', fontsize=12)

# Manually create a legend
legend_elements = [mpatches.Patch(color='b', alpha=0.5, label='Resistor 1'),
                   mpatches.Patch(color='b', alpha=0.5, label='Resistor 2'),
                   mpatches.Patch(color='b', alpha=0.5, label='Resistor 3')]

ax.legend(handles=legend_elements)

# Show the 3D plot
plt.show()

# Print the calculated values
print(f'Total Current (I): {I:.2f} A')
print(f'Equivalent Parallel Resistance (Rp): {Rp:.2f} ohms')
