import numpy as np
import pandas as pd
import sympy as sp
import torch
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objects as go

# Constants
frequency = 120  # Hz
t_values = np.linspace(0, 1, 1000)  # Time values

# Calculate current using I = V/R and sinusoidal voltage
V0 = 1  # Example voltage
R = 1   # Example resistance
I_values = (V0 / R) * np.sin(2 * np.pi * frequency * t_values)

# Calculate power using P = I * V
P_values = I_values * V0

# Create DataFrame for data storage and analysis
data = pd.DataFrame({'Time': t_values, 'Current': I_values, 'Power': P_values})

# Display the first few rows of the DataFrame
print(data.head())

# 3D Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(data['Time'], data['Current'], data['Power'])
ax.set_xlabel('Time')
ax.set_ylabel('Current')
ax.set_zlabel('Power')
plt.show()
