import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import sympy as sp
import torch
import sklearn
import scipy.constants as const

# Given values
voltage = 120  # V
resistance = 0.500  # Ω
mass = 2.00  # g
specific_heat_capacity = 0.200  # cal/g⋅ºC
time = 0.0500  # s

# Calculating current using Ohm's law (I = V/R)
current = voltage / resistance

# Calculating heat transferred (Q = I^2Rt)
heat_transferred = current ** 2 * resistance * time

# Calculating temperature rise (ΔT = Q / (mc))
temperature_rise = heat_transferred / (mass * specific_heat_capacity)

print("Temperature Rise:", temperature_rise, "ºC")

# Generating time values
time_values = np.linspace(0, time, 100)

# Calculate temperature rise at each time point
temperature_rise_values = (current ** 2 * resistance * time_values) / (mass * specific_heat_capacity)

# Creating the 3D visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(time_values, temperature_rise_values, time_values, label='Temperature Rise')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Temperature Rise (ºC)')
ax.set_zlabel('Time (s)')
ax.set_title('Temperature Rise Over Time')
ax.legend()

plt.show()

# Creating a 3D surface plot using Plotly
df = pd.DataFrame({'Time': time_values, 'Temperature Rise': temperature_rise_values})
fig = px.line_3d(df, x='Time', y='Temperature Rise', z='Time', title='Temperature Rise Over Time')
fig.show()
