import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
diameter_cm = 25.0
radius_m = diameter_cm / 100  # Convert to meters
current_A = 100
magnetic_field_T = 2.00

# Calculate the force using the formula F = I * B * L, where L is the length of the tube
length_of_tube_m = sp.Symbol('L')
force = current_A * magnetic_field_T * length_of_tube_m

# Convert the force equation to a numerical function
force_function = sp.lambdify(length_of_tube_m, force, 'numpy')

# Generate values for length_of_tube_m
length_values = np.linspace(0.01, 2.0, 100)  # Vary the length from 1 cm to 2 meters

# Calculate the corresponding force values
force_values = force_function(length_values)

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the force as a function of length
ax.plot(length_values, force_values, zs=0, zdir='z', label='Force (N)')

# Add labels and title
ax.set_xlabel('Length of Tube (m)')
ax.set_ylabel('Force (N)')
ax.set_zlabel(' ')
plt.title('Force vs. Length in an MHD Drive')

# Create a creative visualization by adding a "mathematical dance" element
for i in range(1, len(length_values), 10):
    ax.text(
        length_values[i],
        force_values[i],
        0,
        f'L={length_values[i]:.2f}m',
        fontsize=10,
        color='blue',
        ha='right',
        va='bottom'
    )

# Show the plot
plt.legend()
plt.show()
