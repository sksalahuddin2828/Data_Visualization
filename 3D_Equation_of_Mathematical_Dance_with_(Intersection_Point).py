import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.optimize import fsolve

# Given equations
eq1 = lambda x, y, z: x + y + z - 3
eq2 = lambda x, y, z: x*2 + y**2 + z*2 - 4  # Fixed the typo here
eq3 = lambda x, y, z: x*3 + y**3 + z*3 - 5  # Fixed the typo here

# Numerically solving the equations using fsolve
initial_guess = [1, 1, 1]
sol = fsolve(lambda xyz: [eq1(*xyz), eq2(*xyz), eq3(*xyz)], initial_guess)
x_val, y_val, z_val = sol

# Creating a Pandas DataFrame to display the results
data = {'Variable': ['x', 'y', 'z'],
        'Value': [x_val, y_val, z_val]}
df = pd.DataFrame(data)

# 3D Visualization using Plotly
fig = go.Figure(data=[go.Scatter3d(x=[x_val], y=[y_val], z=[z_val], mode='markers', marker=dict(size=8, color='blue'))])
fig.update_layout(scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="z"),
                  title="Intersection Point",
                  showlegend=False)

# Mathematical dance using NumPy vectorization (with fewer data points)
time_values = np.linspace(0, 2*np.pi, 50)  # Reduced the number of data points
x_dance = np.sin(time_values)
y_dance = np.cos(time_values)
z_dance = time_values**2

# Plotting the creative expressions
plt.figure(figsize=(8, 8))
plt.plot(time_values, x_dance, label="x = sin(t)")
plt.plot(time_values, y_dance, label="y = cos(t)")
plt.plot(time_values, z_dance, label="z = t^2")
plt.xlabel("Time (t)")
plt.ylabel("Value")
plt.title("Mathematical Dance")
plt.legend()

# Displaying the results and the visualizations
print("Solutions:")
print(df)
fig.show()
plt.show()
