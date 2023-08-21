import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
alpha = 0.25  # rad/s^2
omega_0 = 0  # initial angular velocity
omega = 5.0  # final angular velocity
t = 20.0     # seconds
r = 5.0      # meters

# Calculate total angle and distance
delta_theta = omega**2 - omega_0**2 / (2 * alpha)
s = r * delta_theta

# Create a DataFrame to store results
data = {'Time (s)': [t], 'Angular Acceleration (rad/s^2)': [alpha], 'Total Angle (rad)': [delta_theta], 'Distance (m)': [s]}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)

# Visualization
time_vals = np.linspace(0, t, num=100)
theta_vals = omega_0 * time_vals + 0.5 * alpha * time_vals**2

plt.figure(figsize=(10, 6))
plt.plot(time_vals, theta_vals, label=r'$\theta = \omega_0 t + \frac{1}{2}\alpha t^2$')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position (rad)')
plt.title('Angular Position vs Time')
plt.legend()
plt.grid(True)
plt.show()

# 3D Visualization
time_vals = np.linspace(0, t, num=100)
theta_vals = omega_0 * time_vals + 0.5 * alpha * time_vals**2
x_vals = r * np.cos(theta_vals)
y_vals = r * np.sin(theta_vals)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x_vals, y_vals, time_vals, label='Helix Path')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Time (s)')
ax.set_title('3D Helix Path of the Particle')
ax.legend()
plt.show()
