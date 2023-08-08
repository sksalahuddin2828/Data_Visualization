import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate data
x = np.linspace(0, 10, 100)
t = np.linspace(0, 5, 50)
X, T = np.meshgrid(x, t)

# Compute wave function and expressions
y = A * np.sin(k * X - ω * T + ϕ)
velocity = A * k * np.cos(k * X - ω * T + ϕ)
acceleration = -A * ω**2 * np.sin(k * X - ω * T + ϕ)

# Create 3D subplots for wave, velocity, and acceleration
fig = plt.figure()
ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

ax1.plot_surface(X, T, y, cmap='viridis')
ax2.plot_surface(X, T, velocity, cmap='plasma')
ax3.plot_surface(X, T, acceleration, cmap='inferno')

plt.show()

# Generate data for superposition
A1 = 0.8
A2 = 0.6
y1 = A1 * np.sin(k * X - ω * T + ϕ)
y2 = A2 * np.cos(k * X - ω * T + ϕ)

# Create superposition subplot
fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
combined_y = y1 + y2
ax.plot_surface(X, T, combined_y, cmap='cividis')

plt.show()
