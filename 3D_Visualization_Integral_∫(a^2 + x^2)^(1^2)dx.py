# Integral: ∫(a^2 + x^2)^(1/2) dx

import sympy as sp

# Define symbols
x, a = sp.symbols('x a')

# Define the integral
integral_expr = sp.sqrt(a**2 + x**2)

# Perform the integration
integral_result = sp.integrate(integral_expr, x)

print(integral_result)
print("")

import numpy as np
import matplotlib.pyplot as plt

# Define a and create x values
a_value = 2
x_vals = np.linspace(0, 5, 100)

# Compute the integral expression
integral_vals = np.sqrt(a_value**2 + x_vals**2)

# Create the plot
plt.plot(x_vals, integral_vals)
plt.xlabel('x')
plt.ylabel('Integral Value')
plt.title('Integral: ∫(a^2 + x^2)^(1/2) dx')
plt.grid()
plt.show()

import plotly.express as px

# Create a DataFrame
import pandas as pd
df = pd.DataFrame({'x': x_vals, 'integral': integral_vals})

# Create an interactive scatter plot
fig = px.scatter(df, x='x', y='integral', title='Interactive Integral Plot')
fig.show()

from mpl_toolkits.mplot3d import Axes3D

# Create meshgrid
X, A = np.meshgrid(x_vals, np.linspace(0.1, 5, 50))
Z = np.sqrt(A**2 + X**2)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, A, Z)
ax.set_xlabel('x')
ax.set_ylabel('a')
ax.set_zlabel('Integral Value')
plt.title('3D Integral Visualization')
plt.show()
