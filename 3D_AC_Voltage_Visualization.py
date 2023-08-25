import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import plotly.express as px
import torch
import sklearn
import scipy

# Set up matplotlib for 3D visualization
from mpl_toolkits.mplot3d import Axes3D

def ac_voltage(V0, f, t):
    return V0 * np.sin(2 * np.pi * f * t)

t_values = np.linspace(0, 1, 1000)  # Time values from 0 to 1 seconds
V0 = 10  # Peak voltage
f = 50  # Frequency in Hz

voltage_values = ac_voltage(V0, f, t_values)

data = {'Time': t_values, 'Voltage': voltage_values}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 6))
plt.plot(df['Time'], df['Voltage'])
plt.title('AC Voltage Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.show()

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(df['Time'], df['Voltage'], df['Voltage'], label='Voltage Curve')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Voltage (V)')
ax.set_zlabel('Voltage (V)')
ax.set_title('3D Voltage Visualization')
plt.show()

fig = px.line(df, x='Time', y='Voltage', title='Interactive AC Voltage Plot')
fig.show()
