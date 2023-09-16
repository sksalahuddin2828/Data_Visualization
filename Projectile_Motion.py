import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Given values
v = 12
angle_deg = 45
x_horizontal = 15
g = 10

# Convert angle to radians
angle_rad = np.radians(angle_deg)

# Calculate the vertical component using trigonometry
v_vertical = v * np.sin(angle_rad)

# Calculate the time of flight using kinematic equations
t_flight = (2 * v_vertical) / g

# Create a time array for trajectory calculation
t = np.linspace(0, t_flight, num=100)

# Calculate horizontal and vertical positions at each time step
x = x_horizontal * t
y = v_vertical * t - 0.5 * g * t**2

# Create a pandas DataFrame for the trajectory data
trajectory_df = pd.DataFrame({'Time (s)': t, 'Horizontal Position (m)': x, 'Vertical Position (m)': y})

# Visualize the trajectory in 2D
plt.figure(figsize=(10, 6))
plt.plot(x, y)
plt.title('Projectile Motion')
plt.xlabel('Horizontal Position (m)')
plt.ylabel('Vertical Position (m)')
plt.grid(True)
plt.show()
