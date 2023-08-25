import numpy as np
import pandas as pd

# Parameters
V0 = 10  # Peak voltage
f = 50   # Frequency in Hz
R = 5    # Resistance

# Time array
t = np.linspace(0, 0.1, 1000)  # 0 to 0.1 seconds, 1000 data points

# Calculating voltage and current
V = V0 * np.sin(2 * np.pi * f * t)
I = V / R

# Creating a DataFrame
data = {'Time': t, 'Voltage': V, 'Current': I}
df = pd.DataFrame(data)

import sympy as sp

# Define symbols
t_sym = sp.Symbol('t')
V_sym = V0 * sp.sin(2 * sp.pi * f * t_sym)
I_sym = V_sym / R

# Simplify the expression
I_sym_simplified = sp.simplify(I_sym)

print(I_sym_simplified)

import matplotlib.pyplot as plt
import plotly.express as px

# Matplotlib 3D Visualization
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(t, V, I)
ax.set_xlabel('Time')
ax.set_ylabel('Voltage')
ax.set_zlabel('Current')
plt.show()

# Plotly Interactive Plot
fig = px.scatter_3d(df, x='Time', y='Voltage', z='Current', title='Voltage-Current Relationship')
fig.show()
