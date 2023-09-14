import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import plotly.express as px
import torch
from sklearn.linear_model import LinearRegression
from scipy.constants import elementary_charge

# Set up sympy for symbolic math
sp.init_printing()

# Given data
B = 0.200  # Magnetic field strength in Tesla
diameter_aorta = 0.026  # Diameter of aorta in meters
velocity_blood = 0.6  # Blood velocity in m/s

# Calculate the Hall voltage
hall_voltage = B * diameter_aorta * velocity_blood
print(f"Hall Voltage: {hall_voltage} Volts")

# Given data
wingspan = 17.0  # Wingspan in meters
earth_field_strength = 8.00e-5  # Earth's magnetic field strength in Tesla
hall_voltage_aircraft = 1.60  # Hall voltage between wing tips in Volts

# Calculate the speed of the aircraft
speed_aircraft = hall_voltage_aircraft / (earth_field_strength * wingspan)
print(f"Speed of Aircraft: {speed_aircraft} m/s")

# Create a 3D plot of magnetic field lines
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define a grid of points
x = np.linspace(-1, 1, 20)
y = np.linspace(-1, 1, 20)
X, Y = np.meshgrid(x, y)
Z = X * 0  # Assume the field is uniform in the z-direction

# Plot the magnetic field lines
ax.quiver(X, Y, Z, 0, 0, B, length=0.1, normalize=True, color='b')

# Customize the plot appearance
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Magnetic Field Lines')
plt.show()
