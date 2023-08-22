import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Step 2: Calculate Initial and Final Parameters
I = 800.0  # moment of inertia in kg-m^2
initial_angular_velocity = 4.0 * 2 * np.pi  # initial angular velocity in rad/s
final_kinetic_energy = 2.03e5  # final kinetic energy in J

# Calculate new angular velocity
final_angular_velocity = np.sqrt(final_kinetic_energy * 2 / I)

# Step 3: Create Data Visualization
time_values = np.linspace(0, 5, num=100)
kinetic_energy_values = 0.5 * I * initial_angular_velocity**2 * np.exp(-time_values)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the data
ax.plot(time_values, [initial_angular_velocity] * len(time_values), kinetic_energy_values)

# Add labels and title
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Velocity (rad/s)')
ax.set_zlabel('Kinetic Energy (J)')
ax.set_title('Change in Kinetic Energy and Angular Velocity')

# Add LaTeX annotation
ax.text(2, initial_angular_velocity, 200000, r'$KE = \frac{1}{2} I \omega^2 e^{-t}$', fontsize=12, color='red')

# Show the plot
plt.show()
