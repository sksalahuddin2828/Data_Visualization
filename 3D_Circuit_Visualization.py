import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Define circuit parameters
V = 12.0  # Voltage source in volts
R1 = 1.00  # Resistance in ohms
R2 = 6.00  # Resistance in ohms
R3 = 13.0  # Resistance in ohms

# Calculate currents using Ohm's law
I1 = V / R1
I2 = V / R2
I3 = V / R3

# Create symbolic variables for equations
I1_sym, I2_sym, I3_sym = sp.symbols('I1 I2 I3')

# Define equations
eq1 = sp.Eq(I1_sym, I1)
eq2 = sp.Eq(I2_sym, I2)
eq3 = sp.Eq(I3_sym, I3)

# Solve equations symbolically
solutions = sp.solve([eq1, eq2, eq3], (I1_sym, I2_sym, I3_sym))

# Print solutions
print("Current I1:", solutions[I1_sym])
print("Current I2:", solutions[I2_sym])
print("Current I3:", solutions[I3_sym])

# Create a simple 3D visualization of the circuit
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define resistor positions
resistor_positions = [(0, 0, 0), (0, 0, 1), (0, 0, 2)]

# Plot resistors
for i, (x, y, z) in enumerate(resistor_positions):
    ax.plot([x, x], [y, y], [z, z + 0.5], label=f'Resistor {i+1}')

# Add voltage source
ax.text(0, 0, 2.5, f'Voltage Source ({V} V)', fontsize=12, color='blue')

# Customize plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()
ax.set_title('Circuit Visualization')

# Show the plot
plt.show()
