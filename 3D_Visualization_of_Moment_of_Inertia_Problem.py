import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define symbols
m, R, d = sp.symbols('m R d')

# Define equation
equation = sp.Eq(m * d**2, (13 * m * R**2))

# Solve the equation
solution = sp.solve(equation, d)

# Convert solution to numerical values
R_value = 1.0  # Assign a value to R
solution_value = solution[0].subs(R, R_value)

# Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the point representing the center of mass
ax.scatter(0, 0, 0, color='r', marker='o', label='Center of Mass')

# Plot the point representing the object's position
ax.scatter(solution_value, 0, 0, color='b', marker='x', label='Object Position')

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

plt.title('3D Visualization of Moment of Inertia Problem')
plt.show()
