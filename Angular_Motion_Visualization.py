import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
angular_velocity_initial = 0  # rad/s
angular_velocity_final = 2 * np.pi * 40  # rad/s
time = 20.0  # s

# Calculate angular acceleration using numpy
angular_acceleration = (angular_velocity_final - angular_velocity_initial) / time

# Create a time array
time_array = np.linspace(0, time, num=100)

# Calculate angular velocity at different times using linear acceleration equation
angular_velocity_array = angular_velocity_initial + angular_acceleration * time_array

# Create a pandas DataFrame to store the data
data = {'Time (s)': time_array, 'Angular Velocity (rad/s)': angular_velocity_array}
df = pd.DataFrame(data)

# Create an interactive plot using Plotly
fig = px.line(df, x='Time (s)', y='Angular Velocity (rad/s)', title='Angular Motion')
fig.show()

# Create a 3D visualization
fig_3d = plt.figure()
ax_3d = fig_3d.add_subplot(111, projection='3d')

# Generate data points for visualization
t_points = np.linspace(0, time, num=100)
omega_points = angular_velocity_initial + angular_acceleration * t_points
alpha_points = np.full_like(t_points, angular_acceleration)

# Plotting
ax_3d.plot(t_points, omega_points, alpha_points, label='Angular Velocity vs Time')
ax_3d.set_xlabel('Time (s)')
ax_3d.set_ylabel('Angular Velocity (rad/s)')
ax_3d.set_zlabel('Angular Acceleration (rad/s^2)')
ax_3d.set_title('Angular Motion Visualization')
ax_3d.legend()

# Show the plot
plt.show()
