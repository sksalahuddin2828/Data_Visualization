import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve
from mpl_toolkits.mplot3d import Axes3D

# Constants
initial_velocity = 0  # Initial velocity of the bullet
final_velocity = 500  # Bullet velocity in m/s
acceptable_motion = 0.001  # 1.00 mm in meters
capacitance = 600e-6  # Capacitance in Farads

# Symbolic variables for time and resistance
t, R = symbols('t R')

rc_constant_eqn = R * capacitance - 1.00

# Solve for R
resistance_value = solve(rc_constant_eqn, R)[0]

# Using the kinematic equation: final_velocity = initial_velocity + (acceleration * time)
# Assuming constant acceleration, initial_velocity is 0
acceleration = final_velocity / resistance_value
time_to_limit_blurring = final_velocity / acceleration

# Convert time_to_limit_blurring to a float
time_to_limit_blurring = float(time_to_limit_blurring)

# Create a time array for visualization
time_array = np.linspace(0, time_to_limit_blurring, 1000)

# Calculate the motion during time t
motion = 0.5 * acceleration * (time_array**2)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the resistance and motion as a function of time
ax.plot([resistance_value], [time_to_limit_blurring], [acceptable_motion], marker='o', markersize=10, color='r', label='Solution Point')
ax.plot([resistance_value], [time_to_limit_blurring], [0], marker='o', markersize=10, color='g', label='Bullet Path')
ax.plot([resistance_value], [0], [acceptable_motion], marker='o', markersize=10, color='b', label='Motion Limit')

# Labels and legend
ax.set_xlabel('Resistance (R)')
ax.set_ylabel('Time (t)')
ax.set_zlabel('Motion (x)')
ax.set_title('Bullet Motion and Resistance')
ax.legend()

# Show the plot
plt.show()
