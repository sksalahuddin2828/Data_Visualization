import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from sympy import symbols, solve
import matplotlib.pyplot as plt

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

# Create a plotly figure for angular position vs time
time_vals = np.linspace(0, t, num=100)
theta_vals = omega_0 * time_vals + 0.5 * alpha * time_vals**2

fig_angular = px.line(x=time_vals, y=theta_vals, labels={'x': 'Time (s)', 'y': 'Angular Position (rad)'},
                      title='Angular Position vs Time')
fig_angular.show()

# 3D Visualization using Plotly
time_vals = np.linspace(0, t, num=100)
theta_vals = omega_0 * time_vals + 0.5 * alpha * time_vals**2
x_vals = r * np.cos(theta_vals)
y_vals = r * np.sin(theta_vals)

fig_3d = go.Figure(data=[go.Scatter3d(x=x_vals, y=y_vals, z=time_vals, mode='lines', line=dict(color='blue'))])
fig_3d.update_layout(scene=dict(xaxis_title='X (m)', yaxis_title='Y (m)', zaxis_title='Time (s)'),
                     title='3D Helix Path of the Particle')
fig_3d.show()

# Symbolic solution for time when the total angle is reached
t_sym = symbols('t')
eq = omega_0 * t_sym + 0.5 * alpha * t_sym**2 - delta_theta
solution = solve(eq, t_sym)
time_to_reach_angle = solution[1]  # Take the positive solution

print(f"Time taken to reach the total angle: {time_to_reach_angle:.2f} seconds")

# Matplotlib visualization for symbolic solution
time_vals = np.linspace(0, float(time_to_reach_angle), num=100)
theta_vals = omega_0 * time_vals + 0.5 * alpha * time_vals**2

plt.figure(figsize=(10, 6))
plt.plot(time_vals, theta_vals, label=r'$\theta = \omega_0 t + \frac{1}{2}\alpha t^2$')
plt.axvline(x=float(time_to_reach_angle), color='r', linestyle='--', label='Time to reach angle')
plt.xlabel('Time (s)')
plt.ylabel('Angular Position (rad)')
plt.title('Angular Position vs Time')
plt.legend()
plt.grid(True)
plt.show()
