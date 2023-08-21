import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
angular_velocity_initial = 0  # rad/s
angular_velocity_final = 2 * np.pi * 40  # rad/s
time = 20.0  # s

# Calculate angular acceleration using the given formula
angular_acceleration = (angular_velocity_final - angular_velocity_initial) / time

# Print the angular acceleration
print("Angular Acceleration:", angular_acceleration, "rad/s^2")

# Create a time array
time_array = np.linspace(0, time, num=100)

# Calculate angular velocity at different times using linear acceleration equation
angular_velocity_array = angular_velocity_initial + angular_acceleration * time_array

# Create a pandas DataFrame to store the data
data = {'Time (s)': time_array, 'Angular Velocity (rad/s)': angular_velocity_array}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Create a 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate data points for visualization
t_points = np.linspace(0, time, num=100)
omega_points = angular_velocity_initial + angular_acceleration * t_points
alpha_points = np.full_like(t_points, angular_acceleration)

# Plotting
ax.plot(t_points, omega_points, alpha_points, label='Angular Velocity vs Time')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Angular Velocity (rad/s)')
ax.set_zlabel('Angular Acceleration (rad/s^2)')
ax.set_title('Angular Motion Visualization')
ax.legend()

# Show the plot
plt.show()
