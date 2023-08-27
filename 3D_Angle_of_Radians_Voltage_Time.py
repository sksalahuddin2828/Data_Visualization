import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Calculate the time for one complete cycle of 400-Hz AC power
frequency = 400  # in Hertz
time_period = 1 / frequency  # in seconds

# Display the result
print("Time for one complete cycle:", time_period, "seconds")

# Create a symbolic variable for the angle in radians
angle = sp.symbols('angle', real=True)

# Create a function for the AC voltage over time
voltage_function = sp.sin(angle)

# Create a numpy function from the symbolic function
voltage_np = sp.lambdify(angle, voltage_function, 'numpy')

# Generate time values
angles = np.linspace(0, 2*np.pi, 100)
voltages = voltage_np(angles)

# Create a DataFrame using pandas
data = pd.DataFrame({'Angle': angles, 'Voltage': voltages})

# Create a 3D plot using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(data['Angle'], data['Voltage'], np.zeros_like(data['Angle']), 'b')
ax.set_xlabel('Angle (radians)')
ax.set_ylabel('Voltage')
ax.set_zlabel('Time')

plt.show()
