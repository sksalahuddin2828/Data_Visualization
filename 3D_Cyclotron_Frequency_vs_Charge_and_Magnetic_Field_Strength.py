import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.express as px
import sympy as sp
import torch
import sklearn
from scipy.constants import e, m_e

# Problem 1
voltage = 7.50e-4  # Volts

# Problem 3
velocity_a = 1.18e3  # m/s
velocity_b = -1.18e3  # m/s

# Problem 5
voltage_5 = 11.3e-3  # Convert to volts

# Problem 7
voltage_7 = 1.16e-6  # Convert to volts

# Problem 9
magnetic_field_strength = 2.00  # Tesla

# Problem 1: Voltage to Electric Field
electric_field = voltage / 1  # Electric field (E) = Voltage (V) / Distance (d)

# Create a visualization for Problem 1
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(voltage, 1, electric_field, c='r', marker='o')
ax.set_xlabel('Voltage (V)')
ax.set_ylabel('Distance (d)')
ax.set_zlabel('Electric Field (E)')
plt.title('Electric Field vs Voltage and Distance')
plt.show()

# Problem 5: Voltage Conversion
voltage_mV = voltage_5 * 1e3  # Convert to millivolts

# Create a pie chart visualization for Problem 5
labels = ['Voltage (V)', 'Voltage (mV)']
values = [voltage, voltage_mV]
fig = px.pie(names=labels, values=values, title='Voltage Conversion (V to mV)')
fig.show()

# Problem 7: Voltage Conversion
voltage_uV = voltage_7 * 1e6  # Convert to microvolts

# Create a bar chart visualization for Problem 7
df = pd.DataFrame({'Voltage (V)': [voltage], 'Voltage (uV)': [voltage_uV]})
ax = df.plot(kind='bar', title='Voltage Conversion (V to uV)')
ax.set_ylabel('Voltage')
plt.xticks(rotation=0)
plt.show()

# Problem 9: Magnetic Field
# Calculate the cyclotron frequency using SymPy
q = e  # Charge of an electron
m = m_e  # Mass of an electron
B = magnetic_field_strength  # Magnetic field strength
cyclotron_frequency = (q * B) / (2 * np.pi * m)

# Create a 3D surface plot for Problem 9
x = np.linspace(0, 5, 100)
y = np.linspace(0, 5, 100)
X, Y = np.meshgrid(x, y)
Z = (q * X) / (2 * np.pi * m * Y)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')
ax.set_xlabel('Charge (q)')
ax.set_ylabel('Magnetic Field Strength (B)')
ax.set_zlabel('Cyclotron Frequency')
plt.title('Cyclotron Frequency vs Charge and Magnetic Field Strength')
plt.show()
