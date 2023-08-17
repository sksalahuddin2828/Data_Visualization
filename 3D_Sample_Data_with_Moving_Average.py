import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import pandas as pd
import plotly.express as px

# Define symbolic variables and functions
x = sp.symbols('x')
u = sp.Function('u')(x)
f_u = u ** 2 + 3 * u + 1

# Calculate the derivative using Sympy
du_dx = sp.diff(f_u, x)

# Print results
print("Original function f(u):", f_u)
print("Derivative of f(u) with respect to x:", du_dx)

# Generate some sample data
x_values = np.linspace(0, 10, 100)
y_values = np.sin(x_values) + np.random.normal(0, 0.1, 100)

# Create a DataFrame using Pandas
df = pd.DataFrame({'x': x_values, 'y': y_values})

# Calculate moving average using Numpy
window_size = 5
df['moving_average'] = np.convolve(df['y'], np.ones(window_size)/window_size, mode='same')

# Create a dynamic 3D visualization using Matplotlib
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u_vals = np.linspace(-5, 5, 100)
x_vals = np.linspace(0, 10, 100)
U, X = np.meshgrid(u_vals, x_vals)
Z = U ** 2 + 3 * U + 1
ax.plot_surface(X, U, Z, cmap='viridis')
ax.set_xlabel('x')
ax.set_ylabel('u')
ax.set_zlabel('f(u)')

# Create an interactive visualization using Plotly Express
fig_plotly = px.scatter(df, x='x', y='y', title='Sample Data with Moving Average')
fig_plotly.add_scatter(x=df['x'], y=df['moving_average'], mode='lines', name='Moving Average')
fig_plotly.show()
