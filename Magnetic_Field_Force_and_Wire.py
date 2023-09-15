import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
from sympy.plotting import plot3d

B = 1.50  # Magnetic field strength in Tesla
l = 0.05  # Length of the wire in meters (5.00 cm)
I = 20.0  # Current in Amperes

F = I * l * B

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create wire coordinates
wire_coords = np.array([[0, 0, 0], [l, 0, 0]])

# Create magnetic field vector
B_vector = np.array([0, 0, B])

# Plot wire
ax.plot(wire_coords[:, 0], wire_coords[:, 1], wire_coords[:, 2], label='Wire', color='b')

# Plot magnetic field vector
ax.quiver(0, 0, 0, B_vector[0], B_vector[1], B_vector[2], label='Magnetic Field', color='r', linewidth=2)

# Plot force vector
force_vector = np.array([0, F, 0])
ax.quiver(0, 0, 0, force_vector[0], force_vector[1], force_vector[2], label='Force', color='g', linewidth=2)

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set axis limits
ax.set_xlim([0, l])
ax.set_ylim([-1, 1])
ax.set_zlim([0, B])

# Add legend
ax.legend()

# Show the plot
plt.show()

# Define symbols
I_sym, l_sym, B_sym, F_sym = sp.symbols('I l B F')

# Define force equation symbolically
force_eq = sp.Eq(F_sym, I_sym * l_sym * B_sym)

# Substitute values
force_eq = force_eq.subs({I_sym: I, l_sym: l, B_sym: B, F_sym: F})

# Display the equation
sp.init_printing()
display(force_eq)
