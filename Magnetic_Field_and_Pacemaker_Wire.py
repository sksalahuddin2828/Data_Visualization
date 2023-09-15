import numpy as np
import sympy as sp

# Constants
velocity = 0.1  # 10.0 cm/s converted to m/s
length = 0.1  # 10.0 cm converted to meters
induced_voltage = 0.02  # 20.0 mV converted to V

# Symbols
B = sp.symbols('B')

# Faraday's Law equation
eq = sp.Eq(induced_voltage, B * velocity * length)

# Solve for B
magnetic_field_strength = sp.solve(eq, B)[0]

# Convert the result to numeric value
magnetic_field_strength_numeric = magnetic_field_strength.evalf()

print(f"The magnetic field strength is {magnetic_field_strength_numeric:.4f} Tesla")

# Answer: The magnetic field strength is 2.0000 Tesla


#---------------------------------------------------------------------------------------


import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
velocity = 0.1  # 10.0 cm/s converted to m/s
length = 0.1    # 10.0 cm converted to meters
induced_voltage = 0.02  # 20.0 mV converted to V

# Symbols
B = sp.symbols('B')

# Faraday's Law equation
eq = sp.Eq(induced_voltage, B * velocity * length)

# Solve for B
magnetic_field_strength = sp.solve(eq, B)[0]

# Convert the result to a numeric value
magnetic_field_strength_numeric = magnetic_field_strength.evalf()

# Print the result
print(f"The magnetic field strength is {magnetic_field_strength_numeric:.4f} Tesla")

# Create a simple 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define a wire segment
wire_length = np.linspace(0, length, 100)
wire_x = wire_length
wire_y = np.zeros_like(wire_length)
wire_z = np.zeros_like(wire_length)

# Plot the wire segment
ax.plot(wire_x, wire_y, wire_z, label='Pacemaker Wire', lw=2)

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.show()
