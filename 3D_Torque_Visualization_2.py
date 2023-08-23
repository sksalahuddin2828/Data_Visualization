import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Given data
I = 30.0  # kg*m^2
alpha_1 = 12.56  # rad/s^2
alpha_2 = -6.28  # rad/s^2

# Torque calculations
torque_1 = I * alpha_1
torque_2 = I * alpha_2

print("Torque (α = 12.56 rad/s^2):", torque_1)
print("Torque (α = -6.28 rad/s^2):", torque_2)

# Theory Explanation
explanation = (
    "In the first case, where α = 12.56 rad/s², the torque is calculated as:"
    f"\nTorque = I * α = {I} * {alpha_1} = {torque_1:.2f} N⋅m."
    "\n\nIn the second case, where α = -6.28 rad/s², the torque is calculated as:"
    f"\nTorque = I * α = {I} * {alpha_2} = {torque_2:.2f} N⋅m."
)

# 3D Torque Visualization (α = 12.56 rad/s^2)
time_values = np.linspace(0, 1, 100)
torque_values = I * alpha_1 * np.ones_like(time_values)

fig_torque = plt.figure()
ax_torque = fig_torque.add_subplot(111, projection='3d')
ax_torque.plot(time_values, torque_values, zs=0, zdir='y', label='Torque')
ax_torque.set_xlabel('Time')
ax_torque.set_ylabel('Torque')
ax_torque.set_zlabel('Value')
ax_torque.legend()
plt.title('3D Torque Visualization (α = 12.56 rad/s^2)')
plt.show()

# Animation using Matplotlib's FuncAnimation (α = -6.28 rad/s^2)
fig_anim, ax_anim = plt.subplots()
ax_anim.set_xlim(0, 10)
ax_anim.set_ylim(-200, 200)
line, = ax_anim.plot([], [], lw=2)

def animate(i):
    x = time_values[:i+1]
    y = I * alpha_2 * x
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig_anim, animate, frames=len(time_values), interval=100, blit=True)
plt.title('Torque Animation (α = -6.28 rad/s^2)')
plt.xlabel('Time (s)')
plt.ylabel('Torque (N⋅m)')
plt.show()

# Display Theory Explanation
print(explanation)
