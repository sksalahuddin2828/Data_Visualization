import sympy as sp
import numpy as np

# Define symbolic matrices
A = sp.Matrix([[1, 2], [3, 4]])
B = sp.Matrix([[5, 6], [7, 8]])

# Symbolically calculate matrix multiplication
C = A * B

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define matrices and animation function
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

fig, ax = plt.subplots()

def animate(i):
    ax.clear()
    result_matrix = A + (i/10) * (B - A)
    ax.imshow(result_matrix, cmap='coolwarm')
    ax.set_title(f'Animation Step: {i}')
    
ani = FuncAnimation(fig, animate, frames=10, interval=500)
plt.show()

from mpl_toolkits.mplot3d import Axes3D

# Create 3D figure
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define matrices and plot
X, Y = np.meshgrid(np.arange(2), np.arange(2))
Z_A = np.array([[1, 2], [3, 4]])
Z_B = np.array([[5, 6], [7, 8]])

ax.plot_surface(X, Y, Z_A, cmap='viridis')
ax.plot_surface(X, Y, Z_B, cmap='plasma')

plt.show()

import plotly.graph_objects as go

# Create interactive heatmap
trace_A = go.Heatmap(z=A, colorscale='Viridis', zmin=0, zmax=10)
trace_B = go.Heatmap(z=B, colorscale='Plasma', zmin=0, zmax=10)

layout = go.Layout(title='Interactive Heatmap', xaxis=dict(title='Columns'), yaxis=dict(title='Rows'))
fig = go.Figure(data=[trace_A, trace_B], layout=layout)
fig.show()
