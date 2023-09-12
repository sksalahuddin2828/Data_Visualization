import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Given data
q = 20e-9  # Charge in Coulombs
v = 10.0  # Velocity in m/s
B = 5e-5  # Magnetic field strength in Tesla

# Calculate the magnetic force
F = q * v * B

# Create a symbolic variable for the force vector
F_vector = sp.Matrix([0, 0, -F])

# Create a symbolic variable for the velocity vector
v_vector = sp.Matrix([v, 0, 0])

# Create a symbolic variable for the magnetic field vector
B_vector = sp.Matrix([0, 0, B])

# Calculate the cross product of v and B to find the direction of the force
cross_product = v_vector.cross(B_vector)

# Create a figure for 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors
origin = [0, 0, 0]
ax.quiver(*origin, *F_vector, color='r', label='Magnetic Force')
ax.quiver(*origin, *v_vector, color='b', label='Velocity')
ax.quiver(*origin, *B_vector, color='g', label='Magnetic Field')
ax.quiver(*origin, *cross_product, color='k', label='Direction of Force')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set plot limits for better visualization
ax.set_xlim(0, max(F, v))
ax.set_ylim(0, max(F, v))
ax.set_zlim(0, max(F, v))

# Add a legend
ax.legend()

# Show the plot
plt.show()

# Print the calculated force
print(f"The magnetic force is {F:.2e} N.")
