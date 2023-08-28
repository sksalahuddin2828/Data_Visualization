# Calculations and Data Preparation

import numpy as np
import pandas as pd
import sympy as sp

# Given data
frequency = 60  # Hz
Vrms = 1.0      # Root Mean Square voltage

# Calculate time periods
T = 1 / frequency
t_values = np.linspace(0, 2*T, 1000)  # Time values for two periods

# Instantaneous voltage functions
voltage = lambda t: Vrms * np.sin(2 * np.pi * frequency * t)
voltage_negative = lambda t: -Vrms * np.sin(2 * np.pi * frequency * t)

# Calculate times when voltage equals Vrms and -Vrms
t_equal_Vrms = t_values[np.isclose(voltage(t_values), Vrms, atol=1e-2)]
t_equal_negative_Vrms = t_values[np.isclose(voltage_negative(t_values), -Vrms, atol=1e-2)]

# Create a DataFrame for visualization
data = pd.DataFrame({'Time': t_values, 'Voltage': voltage(t_values)})

# Print times
print("Times when voltage equals Vrms:", t_equal_Vrms)
print("Times when voltage equals -Vrms:", t_equal_negative_Vrms)

#----------------------------------------------------------------------------------------------------

# Dynamic and creative visualization

import matplotlib.pyplot as plt
import plotly.express as px
from mpl_toolkits.mplot3d import Axes3D

# 2D Visualization using Plotly
fig = px.line(data, x='Time', y='Voltage', title='Instantaneous Voltage over Time')
fig.update_xaxes(title_text='Time')
fig.update_yaxes(title_text='Voltage')
fig.show()

# 3D Visualization using Matplotlib
fig_3d = plt.figure()
ax = fig_3d.add_subplot(111, projection='3d')
ax.plot(t_values, voltage(t_values), t_values, label='Voltage')
ax.set_xlabel('Time')
ax.set_ylabel('Voltage')
ax.set_zlabel('Time')
ax.set_title('3D Voltage-Time Visualization')
plt.show()
