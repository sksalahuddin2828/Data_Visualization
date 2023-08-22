import numpy as np
import pandas as pd
import plotly.express as px
import sympy as sp
import matplotlib.pyplot as plt
import torch
from sklearn.linear_model import LinearRegression
from matplotlib.animation import FuncAnimation

# Additional Mathematical Concepts
# Define and visualize a quadratic function
x_vals = np.linspace(-10, 10, 100)
y_vals = x_vals**2
plt.plot(x_vals, y_vals)
plt.title('Quadratic Function: $y = x^2$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Advanced Visualizations with Matplotlib
# Create a contour plot of a function
x_vals = np.linspace(-5, 5, 100)
y_vals = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x_vals, y_vals)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contourf(X, Y, Z, levels=20, cmap='viridis')
plt.colorbar()
plt.title('Contour Plot of $z = \\sin(\\sqrt{x^2 + y^2})$')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Animation with Matplotlib
fig, ax = plt.subplots()
x_vals = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x_vals, np.sin(x_vals))

def animate(i):
    line.set_ydata(np.sin(x_vals + i / 10))
    return line,

ani = FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
plt.show()

# 3D Visualizations with Plotly
data = {'x': np.random.rand(100), 'y': np.random.rand(100), 'z': np.random.rand(100)}
df = pd.DataFrame(data)
scatter_3d_fig = px.scatter_3d(df, x='x', y='y', z='z', title='3D Scatter Plot')
scatter_3d_fig.show()

# Symbolic Math and Theory with Sympy
x = sp.Symbol('x')
equation = sp.Eq(x**2 + 3*x + 2, 8)
solution = sp.solve(equation, x)
print("Solution:", solution)

# Interactive Widgets and Exploration
from ipywidgets import interact, widgets

@interact(a=(1, 10))
def plot_sin_wave(a):
    x_vals = np.linspace(0, 2 * np.pi, 100)
    y_vals = np.sin(a * x_vals)
    plt.plot(x_vals, y_vals)
    plt.title(f'Sine Wave with Frequency {a}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

# Integrating Physics Concepts
# Simulate and visualize simple harmonic motion
def simple_harmonic_motion(t, A, f):
    return A * np.sin(2 * np.pi * f * t)

t_vals = np.linspace(0, 10, 100)
plt.plot(t_vals, simple_harmonic_motion(t_vals, A=1, f=0.5))
plt.title('Simple Harmonic Motion')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
