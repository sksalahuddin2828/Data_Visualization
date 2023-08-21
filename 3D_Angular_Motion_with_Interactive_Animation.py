import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from sympy import symbols, Eq, solve
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given values
angular_velocity_initial = 0  # rad/s
angular_velocity_final = 2 * np.pi * 40  # rad/s
time = 20.0  # s

# Calculate angular acceleration using sympy
angular_acceleration_sym = symbols('alpha')
equation = Eq((angular_velocity_final - angular_velocity_initial) / time, angular_acceleration_sym)
angular_acceleration_solution = solve(equation, angular_acceleration_sym)[0]

# Convert angular acceleration to a numerical value
angular_acceleration = float(angular_acceleration_solution)

# Create a time array
time_array = np.linspace(0, time, num=100)

# Calculate angular velocity and displacement at different times
angular_velocity_array = angular_velocity_initial + angular_acceleration * time_array
angular_displacement_array = (
    angular_velocity_initial * time_array + 0.5 * angular_acceleration * time_array ** 2
)

# Create a pandas DataFrame to store the data
data = {
    'Time (s)': time_array,
    'Angular Velocity (rad/s)': angular_velocity_array,
    'Angular Displacement (rad)': angular_displacement_array,
}
df = pd.DataFrame(data)

# Create a subplot with interactive animation and angular velocity/displacement plots
fig = make_subplots(rows=2, cols=1, specs=[[{"type": "scatter"}], [{"type": "scatter"}]])
fig.add_trace(
    go.Scatter(x=df['Time (s)'], y=df['Angular Velocity (rad/s)'], name='Angular Velocity'),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=df['Time (s)'], y=df['Angular Displacement (rad)'], name='Angular Displacement'),
    row=2, col=1
)
fig.update_layout(
    title='Angular Motion with Interactive Animation',
    xaxis_title='Time (s)',
    showlegend=True,
)

# Create a 3D animation of angular motion
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

# Show the plots
fig.show()
plt.show()
