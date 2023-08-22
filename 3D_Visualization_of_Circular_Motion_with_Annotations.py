import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import torch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import scipy.optimize as opt

alpha = 0.25  # rad/s^2
omega_0 = 0  # initial angular velocity in rad/s
omega = 5.0  # final angular velocity in rad/s
t = 20.0  # time in seconds
r = 5.0  # radius in meters

delta_theta = omega ** 2 - omega_0 ** 2 / (2 * alpha)
s = r * delta_theta

# Create a DataFrame for visualization
data = {'Time (s)': [0, t],
        'Angular Velocity (rad/s)': [omega_0, omega]}
df = pd.DataFrame(data)

# Plot angular velocity using Plotly
fig = px.line(df, x='Time (s)', y='Angular Velocity (rad/s)', title='Angular Velocity vs Time')
fig.show()

# Create a 3D visualization using Matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Generate a circle in 3D space
theta = np.linspace(0, delta_theta, 100)
x = r * np.cos(theta)
y = r * np.sin(theta)
z = np.linspace(0, s, 100)

ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Distance')
ax.set_title('3D Visualization of Circular Motion')
plt.show()

# Annotate the 3D plot with equations and labels
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Distance')

# Annotate with equations and labels
ax.text(0, 0, 0, r'$\theta=0$', fontsize=12, color='red')
ax.text(x[-1], y[-1], z[-1], f'({x[-1]:.1f}, {y[-1]:.1f}, {z[-1]:.1f})', fontsize=12, color='blue')

ax.set_title('3D Visualization of Circular Motion with Annotations')
plt.show()
