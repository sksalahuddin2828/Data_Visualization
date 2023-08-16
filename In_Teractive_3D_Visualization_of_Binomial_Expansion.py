import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objs as go
import pandas as pd
from sympy import symbols, expand
from math import factorial
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

# Function to calculate binomial theorem coefficients
def binomial_coefficient(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))

# Function to calculate binomial expansion for (1 + x)^n
def binomial_expansion_positive(x, n):
    return sum(binomial_coefficient(n, k) * x**k for k in range(n + 1))

# Function to calculate binomial expansion for (1 - x)^n
def binomial_expansion_negative(x, n):
    return sum((-1)**k * binomial_coefficient(n, k) * x**k for k in range(n + 1))

# Create x values
x_vals = np.linspace(-0.9, 0.9, 100)

# Positive and negative binomial expansions
n = 5
pos_expansion = [binomial_expansion_positive(x_val, n) for x_val in x_vals]
neg_expansion = [binomial_expansion_negative(x_val, n) for x_val in x_vals]

# Create beautiful plot using Matplotlib
plt.figure(figsize=(10, 6))
plt.plot(x_vals, pos_expansion, label=f"(1 + x)^{n}")
plt.plot(x_vals, neg_expansion, label=f"(1 - x)^{n}")
plt.xlabel('x')
plt.ylabel('Expansion Value')
plt.title(f"Binomial Expansion (n = {n})")
plt.legend()
plt.grid()
plt.show()

# Interactive 3D Visualization using Plotly
n_values = [2, 4, 6, 8, 10]
x_vals_3d = np.linspace(-1, 1, 100)
y_vals_3d = np.linspace(-1, 1, 100)
x_vals_3d, y_vals_3d = np.meshgrid(x_vals_3d, y_vals_3d)

fig_3d = go.Figure()

for n_val in n_values:
    z_vals_3d = np.array([[binomial_expansion_positive(x, n_val) for x in row] for row in x_vals_3d])
    surface = go.Surface(x=x_vals_3d, y=y_vals_3d, z=z_vals_3d, name=f"(1 + x)^{n_val}")
    fig_3d.add_trace(surface)

fig_3d.update_layout(scene=dict(xaxis_title='x', yaxis_title='y', zaxis_title='Expansion Value'),
                      title='Interactive 3D Visualization of Binomial Expansion')
fig_3d.show()
