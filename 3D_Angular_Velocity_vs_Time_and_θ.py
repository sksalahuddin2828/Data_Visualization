import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import torch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
rpm = 7000.0
t = 10.0
alpha_t = 73.3

# Calculate angular velocity (ω) and angular displacement (Δθ)
omega = rpm * (2 * np.pi) / 60
delta_theta = omega ** 2 - 0 ** 2 / (2 * alpha_t)

# Create a DataFrame for equations and values
data = {'Equation': ['7000rpm', 'α', 'Δθ'],
        'Value': [rpm, alpha_t, delta_theta]}
equation_df = pd.DataFrame(data)

# Create a 3D plot using matplotlib
theta_values = np.linspace(0, 2 * np.pi, 100)
time_values = np.linspace(0, t, 100)
theta, time = np.meshgrid(theta_values, time_values)
angular_velocity = omega + alpha_t * time
theta_dot = omega * time + 0.5 * alpha_t * time ** 2

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(theta, time, angular_velocity, cmap='viridis')
ax.set_xlabel('θ (rad)')
ax.set_ylabel('Time (s)')
ax.set_zlabel('Angular Velocity (rad/s)')
ax.set_title('Angular Velocity vs. Time and θ')
