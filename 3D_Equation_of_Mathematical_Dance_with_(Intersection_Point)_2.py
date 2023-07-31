import numpy as np
import sympy as sp
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from scipy.optimize import fsolve

# Define variables x, y, and z using SymPy symbols
x, y, z = sp.symbols('x y z')

# Given equations
eq1 = x + y + z - 3
eq2 = x*2 + y**2 + z*2 - 4  # Fixed the typo here
eq3 = x*3 + y**3 + z*3 - 5  # Fixed the typo here

# Numerically solving the equations using fsolve
eq1_func = sp.lambdify((x, y, z), eq1)
eq2_func = sp.lambdify((x, y, z), eq2)
eq3_func = sp.lambdify((x, y, z), eq3)

def equations(variables):
    x, y, z = variables
    return [eq1_func(x, y, z), eq2_func(x, y, z), eq3_func(x, y, z)]

initial_guess = [1, 1, 1]
sol = fsolve(equations, initial_guess)
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

# Mathematical dance with more complex expressions and functions
time_values = np.linspace(0, 2*np.pi, 100)
x_dance = np.sin(2*time_values) + np.cos(3*time_values) + np.tan(4*time_values)
y_dance = np.exp(-time_values) * np.sin(5*time_values)
z_dance = np.log(1 + np.abs(np.sin(time_values))) * np.sqrt(time_values)

# Plotting the creative expressions
plt.figure(figsize=(8, 8))
plt.plot(time_values, x_dance, label="x = sin(2t) + cos(3t) + tan(4t)")
plt.plot(time_values, y_dance, label="y = e^(-t) * sin(5t)")
plt.plot(time_values, z_dance, label="z = ln(1 + |sin(t)|) * sqrt(t)")
plt.xlabel("Time (t)")
plt.ylabel("Value")
plt.title("Mathematical Dance")
plt.legend()

# Displaying the results and the visualizations
print("Solutions:")
print(df)
fig.show()
plt.show()
