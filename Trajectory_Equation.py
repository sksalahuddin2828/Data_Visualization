import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp

# Constants
theta_deg = 30  # Angle in degrees
v0 = 6  # Initial velocity in m/s
g = 9.8  # Acceleration due to gravity in m/s^2

# Convert angle to radians
theta_rad = np.deg2rad(theta_deg)

# Time of flight
t_flight = (2 * v0 * np.sin(theta_rad)) / g

# Create a time array
t = np.linspace(0, t_flight, num=100)

# Calculate x and y coordinates
x = (v0 * np.cos(theta_rad)) * t
y = (v0 * np.sin(theta_rad)) * t - (0.5 * g * t**2)

# Create a DataFrame for the trajectory data
trajectory_data = pd.DataFrame({'Time (s)': t, 'X (m)': x, 'Y (m)': y})

# Print the trajectory equation
x_sym, y_sym, t_sym = sp.symbols('x y t')
trajectory_eq = sp.Eq(y_sym, x_sym * sp.tan(theta_rad) - (g * x_sym**2) / (2 * v0**2 * sp.cos(theta_rad)**2))
print(f"Trajectory Equation: {sp.pretty(trajectory_eq)}")

# Create a 3D visualization
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, t, label='Projectile Path')
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Time (s)')
ax.set_title('Projectile Motion')
plt.legend()

# Show the plot
plt.show()
