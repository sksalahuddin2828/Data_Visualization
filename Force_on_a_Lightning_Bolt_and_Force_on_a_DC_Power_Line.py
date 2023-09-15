import numpy as np

# Constants
I = 20000  # Current in Amperes
B = 3.00e-5  # Magnetic field in Tesla
L = 1.0  # Length of the wire in meters (for problem 4)
Theta = 30  # Angle in degrees (for problem 5)

# (a) Calculate the force per meter for problem 4
F_per_meter = I * B

# (a) Calculate the force on a 100-m section of the line for problem 5
F_total = I * B * 100  # Force on 100-meter section

# (b) For problem 4(b) - Visualization using Matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the vectors for current (I) and Earth's field (B)
I_vector = np.array([0, 0, I])
B_vector = np.array([0, B, 0])

# Calculate the force vector (F) for problem 4(b)
F_vector = np.cross(I_vector, B_vector)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the vectors
ax.quiver(0, 0, 0, I_vector[0], I_vector[1], I_vector[2], color='blue', label='Current (I)')
ax.quiver(0, 0, 0, B_vector[0], B_vector[1], B_vector[2], color='red', label='Earth\'s Field (B)')
ax.quiver(0, 0, 0, F_vector[0], F_vector[1], F_vector[2], color='green', label='Force (F)')

# Set axis labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Set axis limits
ax.set_xlim([-1, 1])
ax.set_ylim([-1, 1])
ax.set_zlim([-1, 1])

# Add a legend
ax.legend()

# Show the plot
plt.show()

# (b) Discussion of practical concerns (problem 5(b))
print("Discussion of Practical Concerns for Problem 5(b):")
print("The force on the power line due to the magnetic field can lead to mechanical stress on the line.")
print("The angle at which the line is oriented relative to the magnetic field affects the magnitude of the force.")
print("In this case, the force is not parallel or antiparallel to the line, causing it to experience both tension and bending.")
