import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define resistor values
R1 = 10  # Ohms
R2 = 20  # Ohms

# Create a figure and a 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create points for the resistors in series
x_series = [0, R1]
y_series = [0, 0]
z_series = [0, 0]

# Create points for the resistors in parallel
x_parallel = [0, R1, R1 + R2]
y_parallel = [0, 0, 0]
z_parallel = [0, 0, 0]

# Plot the resistors in series
ax.plot(x_series, y_series, z_series, label='Resistors in Series', marker='o')

# Plot the resistors in parallel
ax.plot(x_parallel, y_parallel, z_parallel, label='Resistors in Parallel', marker='^')

# Add labels and legend
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Resistors Visualization')
ax.legend()

# Show the 3D plot
plt.show()
