import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D
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

# Create a DataFrame for visualization
data = {'Position (m)': np.linspace(0, diameter_m, 10),
        'Velocity (m/s)': np.full(10, average_fluid_velocity)}
df = pd.DataFrame(data)

# Plot using Plotly
fig = px.line(df, x='Position (m)', y='Velocity (m/s)', title='Fluid Velocity Profile in the Pipe')
fig.update_xaxes(title_text='Position (m)')
fig.update_yaxes(title_text='Velocity (m/s)')
fig.show()

# Create a 3D vector plot
x = np.linspace(0, diameter_m, 10)
y = np.linspace(0, diameter_m, 10)
z = np.linspace(0, diameter_m, 10)

X, Y, Z = np.meshgrid(x, y, z)

B_x = np.zeros_like(X) + field_T
B_y = np.zeros_like(Y)
B_z = np.zeros_like(Z)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.quiver(X, Y, Z, B_x, B_y, B_z, length=average_fluid_velocity * 0.1, normalize=True, color='b', label='Magnetic Field')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Magnetic Field and Fluid Velocity')

# Create an annotation for fluid velocity
ax.text(diameter_m / 2, 0, 0, f'Average Fluid Velocity: {average_fluid_velocity:.2f} m/s', color='r', fontsize=12)
plt.show()
