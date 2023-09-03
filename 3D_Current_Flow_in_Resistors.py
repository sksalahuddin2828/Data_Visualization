import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Define the given values
V = 12.0  # Voltage output of the battery (in volts)
R1 = 1.00  # Resistance of R1 (in ohms)
R2 = 6.00  # Resistance of R2 (in ohms)
R3 = 13.0  # Resistance of R3 (in ohms)

# (a) Calculate total resistance (Rp) for the parallel connection
Rp_inv = 1 / R1 + 1 / R2 + 1 / R3
Rp = 1 / Rp_inv
Rp = round(Rp, 3)  # Round to three decimal places

# (b) Calculate total current (I)
I = V / Rp

# (c) Calculate currents in each resistor
I1 = V / R1
I2 = V / R2
I3 = V / R3

# (d) Calculate power dissipated by each resistor
P1 = I1 ** 2 * R1
P2 = I2 ** 2 * R2
P3 = I3 ** 2 * R3

# (e) Calculate power output of the source
P_source = V * I

# Create a symbolic expression for Rp using SymPy
R_p = sp.Rational(1, 1) / (sp.Rational(1, R1) + sp.Rational(1, R2) + sp.Rational(1, R3))

# Visualization: Create a 3D representation of resistors and currents
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Resistors
resistor_positions = np.array([(0, 0, 0), (0, 1, 0), (0, 2, 0)])
resistor_labels = ['R1', 'R2', 'R3']

# Currents
current_magnitudes = [I1, I2, I3]

for i, (x, y, z) in enumerate(resistor_positions):
    ax.text(x, y, z, resistor_labels[i], fontsize=12, ha='center', va='center')
    ax.bar3d(x, y, z, 0.1, 0.1, current_magnitudes[i], shade=True, color='blue')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Current (A)')
ax.set_title('Current Flow in Resistors')

plt.show()

# Print results
print(f"(a) Total Resistance (Rp): {Rp} ohms")
print(f"(b) Total Current (I): {I:.2f} A")
print(f"(c) Currents in each resistor:")
print(f"   - R1: {I1:.2f} A")
print(f"   - R2: {I2:.2f} A")
print(f"   - R3: {I3:.2f} A")
print(f"(d) Power Dissipated by each resistor:")
print(f"   - R1: {P1:.2f} W")
print(f"   - R2: {P2:.2f} W")
print(f"   - R3: {P3:.2f} W")
print(f"(e) Power Output of the Source: {P_source:.2f} W")
