# y = x tan θ − gx2/2v2 cos2 θ

import sympy as sp

x, θ, g, v = sp.symbols('x θ g v')
y = x * sp.tan(θ) - (g * x**2) / (2 * v**2 * sp.cos(θ)**2)

print(y)

# Define a function to calculate y
def calculate_y(x_val, θ_val, g_val, v_val):
    y_val = y.subs({x: x_val, θ: θ_val, g: g_val, v: v_val})
    return y_val

import numpy as np

# Generate data
x_values = np.linspace(0, 10, 100)  # Replace with your desired range
θ_values = np.radians(np.linspace(0, 90, 100))  # Angle in radians
g_value = 9.81  # Acceleration due to gravity
v_value = 10  # Initial velocity

y_values = np.array([calculate_y(x_val, θ_val, g_value, v_value) for x_val, θ_val in zip(x_values, θ_values)])

print(y_values)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x_values, θ_values, y_values, c=y_values, cmap='viridis')
ax.set_xlabel('X')
ax.set_ylabel('θ (radians)')
ax.set_zlabel('Y')
plt.show()
