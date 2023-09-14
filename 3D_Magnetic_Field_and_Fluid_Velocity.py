import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import torch
import plotly.express as px
from sklearn.linear_model import LinearRegression
from scipy.optimize import curve_fit

# Constants
diameter_cm = 3.00  # cm
field_T = 0.500  # T
hall_voltage_mv = 60.0  # mV

# Convert units
diameter_m = diameter_cm / 100
hall_voltage_v = hall_voltage_mv / 1000

# Calculate fluid velocity
hall_coefficient = hall_voltage_v / (field_T * diameter_m)
average_fluid_velocity = hall_coefficient * field_T

# Define points in the pipe
x = np.linspace(0, diameter_m, 10)
y = np.linspace(0, diameter_m, 10)
z = np.linspace(0, diameter_m, 10)

# Create a meshgrid for 3D visualization
X, Y, Z = np.meshgrid(x, y, z)

# Define the magnetic field vector
B_x = np.zeros_like(X) + field_T
B_y = np.zeros_like(Y)
B_z = np.zeros_like(Z)

# Create a 3D vector plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, B_x, B_y, B_z, length=average_fluid_velocity * 0.1, normalize=True, color='b', label='Magnetic Field')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Magnetic Field and Fluid Velocity')
plt.show()
