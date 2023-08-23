import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given data
I = 30.0  # kg*m^2
alpha_1 = 12.56  # rad/s^2

# Calculate torque using numeric calculations
torque_1 = I * alpha_1

# Display numeric torque value
print("Torque (α = 12.56 rad/s^2):", torque_1)

# 3D Torque Visualization
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
